<template>
  <UnderDeveloping site-name=""></UnderDeveloping>

  <div class="viewContainer">
      <div class="audioUpload container text-center">
          <div class="audioPlaceholder">
              <div v-if="!file" class="audioUploadLabel">
                  <div class="uploadIconContainer">
                    <img alt="Upload icon" class="uploadIcon" src="../../assets/img/uploadImageIcon.png">
                  </div>
                  Drag audio or click to upload file!
              </div>
              <div v-else>
                  <div class="uploadedAudioContainer">
                      <audio controls id="uploadedAudioPreview" class="uploadedAudioPreview" :src="fileUrl"></audio>
                  </div>
              </div>
              <input type="file" class="audioUploadArea" id="file" ref="file" accept="audio/*" v-on:change="handleFileUpload()" />
              
          </div>

          <div class="container">
              <div class="row buttonsRow px-0">

                  <div class="col-md-3 col-sm-12 px-0 mt-4">
                    <button v-on:click="clear()" class="btn btn-danger text-center w-100 button_border_animation" type="button">Clear 💀</button>
                  </div>

                  <div class="col-md-3 col-sm-12 offset-md-6 px-0 mt-4">
                    <button v-on:click="submitFile()" class="btn btn-success text-center w-100 button_border_animation" type="button">Submit ➣</button>
                  </div>

              </div>

          </div>
      </div>
      <div v-if="audioText && file" class="audioText">
        <h2>Transcribed audio:</h2>
          {{ audioText }}
      </div>
  </div>
</template>

<script>
// @ is an alias to /src  
import UnderDeveloping from '@/components/UnderDeveloping.vue';
import axios from 'axios'

export default {
  name: 'SpeechToTextView',
  components: {
      UnderDeveloping
  },
  data() {
      return {
          file: undefined,
          fileUrl: undefined,
          audioText: undefined,
          audioUploaded: false
      }
  },
  methods: {
      handleFileUpload() {
          this.file = this.$refs.file.files[0];
          this.audioUploaded = true;

          if (!this.file) {
              return;
          }

          this.fileUrl = (window.URL || window.webkitURL).createObjectURL(this.file);
          URL.revokeObjectURL(this.file)
      },
      submitFile() {
          let formData = new FormData();

          formData.append('file', this.file);

          axios.post('/transcribe_audio', formData, {
              headers: {
                  'Content-Type': 'multipart/form-data'
              }
          }).then(response => {
              const data = response.data;

              if (!data) {
                  alert("An error occurred while transcribing the audio.");
                  return;
              }

              this.audioText = response.data;

          }).catch(error => {
              console.error(error);
          });

      },
      clear() {
          this.file = undefined;
          this.fileUrl = undefined;
          this.audioText = undefined;
          this.audioUploaded = false;
      },

      startAnimation(event) {
      const button = event.target;
      button.classList.add('animate');
    },
    stopAnimation(event) {
      const button = event.target;
      button.classList.remove('animate');
    }
  }
}
</script>

<style>

@import '../../styles/buttons_styles.css';


.imageUpload {
    /* margin: 0 auto; */
    /* margin-top: 15%; */
    display: inline-block;
}

.viewContainer {
    margin: 0 auto;
    margin-top: 15%;
    display: flex;
}

.audioText{
    display: inline-block;
    height: 500px;
    width: 500px;
    background-color: rgb(30, 30, 30) !important;
    border: 2px solid rgb(255, 255, 255);
    padding: 1em;
    color: white;
}

.imageUploadArea {
    opacity: 0;
    width: 100%;
    height: 100%;
    margin: 0;
    padding: 0;
}

.imageUploadLabel {
    width: 100%;
    height: 0;
    text-align: center;
    line-height: 450px;
    color: rgba(200, 200, 200, 0.9);
}

.uploadIcon {
    width: 50px;
    height: 50px;
    margin: 0 auto;
}

.uploadIconContainer {
    width: 100%;
    height: 0px;
    padding-bottom: 40px;
}

.uploadedImageContainer {
    width: 100%;
    height: 0px;
    line-height: 495px;
}

.uploadedImagePreview {
    max-width: 500px;
    max-height: 500px;
    width: auto;
    height: auto;
}

.imagePlaceholder {

    margin: 0 auto;

    width: 500px;
    height: 500px;
}

.imagePlaceholderSquare {

    background:
        linear-gradient(to right, rgba(200, 200, 200, 1) 4px, transparent 4px) 0 0,
        linear-gradient(to right, rgba(200, 200, 200, 1) 4px, transparent 4px) 0 100%,
        linear-gradient(to left, rgba(200, 200, 200, 1) 4px, transparent 4px) 100% 0,
        linear-gradient(to left, rgba(200, 200, 200, 1) 4px, transparent 4px) 100% 100%,
        linear-gradient(to bottom, rgba(200, 200, 200, 1) 4px, transparent 4px) 0 0,
        linear-gradient(to bottom, rgba(200, 200, 200, 1) 4px, transparent 4px) 100% 0,
        linear-gradient(to top, rgba(200, 200, 200, 1) 4px, transparent 4px) 0 100%,
        linear-gradient(to top, rgba(200, 200, 200, 1) 4px, transparent 4px) 100% 100%;

    background-repeat: no-repeat;
    background-size: 20px 20px;
}

.buttonsRow {
    width: 500px;
    margin: 0 auto !important;
}



@media screen and (min-width: 400px) and (max-width: 768px) {
    .uploadedImagePreview {
        max-width: 300px;
        max-height: 300px;
    }

    .imagePlaceholder {
        width: 300px;
        height: 300px;
    }

    .imageUploadLabel {
        line-height: 280px;
    }

    .buttonsRow {
        width: 300px;
    }

    .uploadedImageContainer {
        line-height: 295px;
    }
}

@media screen and (min-width: 768px) and (max-width: 1000px) {
    .uploadedImagePreview {
        max-width: 400px;
        max-height: 400px;
    }

    .imagePlaceholder {
        width: 400px;
        height: 400px;
    }

    .imageUploadLabel {
        line-height: 375px;
    }

    .buttonsRow {
        width: 400px;
    }

    .uploadedImageContainer {
        line-height: 395px;
    }
}
</style>
