
<template>
  <div>
    <md-steppers :md-active-step.sync="active" md-linear>
      <md-step id="first" md-label="First Step" md-description="Introduction" :md-done.sync="first">
        <p>This is a object detection annotation viewer that takes inputs in coco json format. It displays bounding boxes with different colors around the object along with their labels</p>
        <p>In the next step please select two categories</p>
        <md-button class="md-raised md-primary" @click="setDone('first', 'second')">Continue</md-button>
      </md-step>
      <md-step
        id="second"
        md-label="Second Step"
        :md-error="secondStepError"
        :md-done.sync="second"
      >
        <div class="md-layout md-gutter">
          <div class="md-layout-item">
            <p>
              Please select only two categories. Example - Person,Dog
              <md-field>
                <label for="movies">Categories</label>
                <md-select v-model="selectedCat" multiple>
                  <md-option v-for="item in cat" v-bind:key="item" :value="item">{{item}}</md-option>
                </md-select>
              </md-field>
            </p>
            <p></p>
          </div>
        </div>
        <md-button class="md-raised md-primary" @click="created()">Continue</md-button>
        <p style="color:red">{{errorMessage}}</p>
        <div v-if="loading">
          <md-progress-spinner :md-diameter="60" :md-stroke="10" md-mode="indeterminate"></md-progress-spinner>
        </div>
      </md-step>

      <md-step id="third" md-label="Third Step" :md-done.sync="third">
        <div class="row">
          <expandable-image class="image" :src="require('../../Output/image0.jpg')" />
          <expandable-image class="image" :src="require('../../Output/image1.jpg')" />
          <expandable-image class="image" :src="require('../../Output/image2.jpg')" />
          <expandable-image class="image" :src="require('../../Output/image3.jpg')" />
          <expandable-image class="image" :src="require('../../Output/image4.jpg')" />
          <expandable-image class="image" :src="require('../../Output/image5.jpg')" />
          <expandable-image class="image" :src="require('../../Output/image6.jpg')" />
          <expandable-image class="image" :src="require('../../Output/image7.jpg')" />
        </div>
        <md-button class="md-raised md-primary" @click="setDone('third')">Done</md-button>
      </md-step>
    </md-steppers>
  </div>
</template>

<script>
export default {
  name: "Stepper",

  data: () => ({
    active: "first",
    first: false,
    second: false,
    third: false,
    secondStepError: null,
    selectedCat: [],
    errorMessage: null,
    loading: false,
    cat: [
      "person",
      "bicycle",
      "car",
      "motorcycle",
      "airplane",
      "bus",
      "train",
      "truck",
      "boat",
      "bench",
      "bird",
      "cat",
      "dog",
      "horse",
      "sheep",
      "cow",
      "elephant",
      "bear",
      "zebra",
      "giraffe",
      "backpack",
      "umbrella",
      "handbag",
      "tie",
      "suitcase",
      "frisbee",
      "skis",
      "snowboard",
      "kite",
      "skateboard",
      "surfboard",
      "bottle",
      "cup",
      "fork",
      "knife",
      "spoon",
      "bowl",
      "banana",
      "apple",
      "sandwich",
      "orange",
      "broccoli",
      "carrot",
      "pizza",
      "donut",
      "cake",
      "chair",
      "couch",
      "bed",
      "toilet",
      "tv",
      "laptop",
      "mouse",
      "remote",
      "keyboard",
      "microwave",
      "oven",
      "toaster",
      "sink",
      "refrigerator",
      "book",
      "clock",
      "vase",
      "scissors",
      "toothbrush",
    ],
  }),

  methods: {
    doAjax() {
      this.isLoading = true;
      // simulate AJAX
      setTimeout(() => {
        this.isLoading = false;
      }, 5000);
    },
    onCancel() {
      console.log("User cancelled the loader.");
    },
    created() {
      this.loading = true;
      const call =
        "http://localhost:5000/api/images/?a=" +
        this.selectedCat[0] +
        "&b=" +
        this.selectedCat[1];

      fetch(call)
        .then(async (response) => {
          if (!response.ok) {
            this.errorMessage = response.text;
          } else {
            this.second = true;
            this.active = "third";
            this.loading = false;
          }
        })
        .catch((error) => {
          this.errorMessage = error;
          console.error("There was an error!", error);
          this.loading = false;
        });
    },
    setDone(id, index) {
      this[id] = true;
      if (index) {
        this.active = index;
      }
    },
    setError() {
      this.secondStepError = "This is an error!";
    },
  },
  mounted() {
    const viewportMeta = document.createElement("meta");
    viewportMeta.name = "viewport";
    viewportMeta.content = "width=device-width, initial-scale=1";
    document.head.appendChild(viewportMeta);
  },
};
</script>

<style scoped>
.md-field {
  max-width: 500px;
}

#app {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  width: 600px;
  max-width: 100%;
  margin: 50px auto;
  position: relative;
}
.image {
  width: 240px;
  max-width: 100%;
}
.row {
  display: flex;
  flex-wrap: wrap;
  padding: 0 40px;
}
</style>