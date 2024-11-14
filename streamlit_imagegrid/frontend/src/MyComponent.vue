<template>
<PerfectScrollbar>
  <justified-infinite-grid
    class="container"
    :gap="5"
    v-bind:gap="gap"
    v-bind:defaultDirection="defaultDirection"
    :columnRange="computedColumnRange"
    v-bind:rowRange="rowRange"
    v-bind:sizeRange="sizeRange"
    v-bind:isCroppedSize="isCroppedSize"
    v-bind:displayedRow="displayedRow"
    v-bind:stretch="stretch"
    v-bind:stretchRange="stretchRange"
    v-bind:passUnstretchRow="passUnstretchRow"
    @request-append="onRequestAppend"
  >
    <div
      class="item"
      v-for="item in items"
      :key="item.key"
      :data-grid-groupkey="item.groupKey"
    >
      <div class="thumbnail" @click="onClicked(urls[item.key])" data-grid-width="100" data-grid-height="100">
        <!-- Check if the file is an image or video -->
        <template v-if="isImage(fixed_urls[item.key]['src'])">
          <img
            :src="fixed_urls[item.key]['src']"
            alt="egjs"
            data-grid-maintained-target="true"
            width="100%"
          />
        </template>
        <template v-else-if="isVideo(fixed_urls[item.key]['src'])">
          <video
            :src="fixed_urls[item.key]['src']"
            controls
            data-grid-maintained-target="true"
            width="100%"
            preload="metadata"
          ></video>
        </template>
      </div>
      <div class="info"> {{ fixed_urls[item.key]['tag'] }}</div>
    </div>
  </justified-infinite-grid>
</PerfectScrollbar>
</template>

<script>
import { ref, watch, onMounted, computed} from "vue";
import { Streamlit } from "streamlit-component-lib";
import { useStreamlit } from "./streamlit";
import { JustifiedInfiniteGrid } from "@egjs/vue3-infinitegrid";
import { PerfectScrollbar } from 'vue3-perfect-scrollbar';

let clickedImageValue = null;
let clickedItem = null;

export default {
  name: "MyComponent",
  components: {
    JustifiedInfiniteGrid,
  },
  props: ["args"],
  setup(props) {
    useStreamlit();
    const container = ref(null);
    const numClicks = ref(0);
    const urls = ref(props.args.urls);
    const fixed_urls = [];
    const zoom = ref(props.args.zoom);
    
    const onClicked = (item) => {
      const clickedItem = typeof item === 'object' ? JSON.stringify(item) : item;
      Streamlit.setComponentValue(clickedItem);;
    };
    const isVideo = (url) => {
      return /\.(mp4|webm|ogg)$/i.test(url);
    };
    const isImage = (url) => {
      return /\.(jpg|jpeg|png|gif|bmp)$/i.test(url);
    };
    const computedColumnRange = computed(() => [zoom.value, zoom.value]);

    watch(() => props.args.zoom, (newZoom) => {
      zoom.value = newZoom;
    });
    return {
      isVideo,
      isImage,
      numClicks,
      onClicked,
      container,
      urls,
      fixed_urls,
      computedColumnRange,
    };
  },
  data() {
    this.fixed_urls = this.conditionUrlInputs(this.urls);
    return {
      items: this.getItems(0, this.urls.length),
      gap: 5,
      defaultDirection: "end",
      columnRange: [this.zoom, this.zoom],
      rowRange: [1, 10],
      sizeRange: [200, 500],
      isCroppedSize: false,
      displayedRow: -1,
    };
  },
  watch: {
    'args.urls': {
      handler(newUrls) {
        this.urls = newUrls;
        this.fixed_urls = this.conditionUrlInputs(newUrls);
        this.items = this.getItems(0, this.fixed_urls.length);
      },
      deep: false,
      immediate: false
    }
  },
  methods: {
    conditionUrlInputs(urls) {
      if (urls.length === 0) {
        return [];
      }
      urls = urls.map(url => {
  if (typeof url === 'string') {
    return { src: url };
  } else if (typeof url === 'object') {
    const { src, ...otherKeys } = url;
    console.log(otherKeys);
    const tag = Object.keys(otherKeys).map(key => `${key}: ${otherKeys[key]}`).join(', ');
    console.log(tag);
    return { src, tag };
  }
});
      return urls;
    },
    getItems(nextGroupKey, count) {
      const nextItems = [];
      for (let i = 0; i < count; ++i) {
        const nextKey = nextGroupKey * count + i;
        nextItems.push({ groupKey: nextGroupKey, key: nextKey });
      }
      return nextItems;
    },
    onRequestAppend(e) {
      const nextGroupKey = (e.groupKey || 0) + 1;
      if (nextGroupKey + 1 > this.urls.length / 10) {
        return;
      }
      this.items = [...this.items, ...this.getItems(nextGroupKey, 10)];
    },
  },
};
</script>

<style>
@import 'vue3-perfect-scrollbar/style.css';

html, body {
  position: relative;
  height: 100%;
}

.container {
  overflow: hidden;
}

.item {
  position: absolute;
  width: 100px;
  /* border: 1px solid #ccc; */
  color: white;
  text-align: center;
}
.ps {
  height: 1000px; /* or max-height: 400px; */
}
</style>