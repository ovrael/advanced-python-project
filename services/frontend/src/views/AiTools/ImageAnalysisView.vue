<template>
    <UnderDeveloping site-name=""></UnderDeveloping>

    <div class="viewContainer">
        <div class="imageUpload container text-center">
            <div class="imagePlaceholder" :class="{ 'imagePlaceholderSquare': !file && !imageUploaded }">
                <div v-if="!file && !imageUploaded" class="imageUploadLabel">
                    <div class="uploadIconContainer">
                        <img alt="Upload icon" class="uploadIcon" src="../../assets/img/uploadImageIcon.png">
                    </div>
                    Drag image or click to upload file!
                </div>
                <div v-else>
                    <div class="uploadedImageContainer">
                        <img alt="Uploaded image" id="uploadedImagePreview" class="uploadedImagePreview" :src="fileUrl">
                    </div>
                </div>
                <input type="file" class="imageUploadArea" id="file" ref="file" accept="image/png, image/gif, image/jpeg" v-on:change="handleFileUpload()" />
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

            <div class="loading" v-if="loading">
                <p>Loading...</p>
                <img v-if="loading" :src="require('@/assets/img/Image_Analysis.svg')" alt="Loading Icon" />
            </div>
        </div>
        
        <div v-if="detectedObjects.length > 0 && file" class="detectedObjects fade-in">
             <img :src="require('@/assets/img/Image_Analysis.svg')" alt="Loading Icon" />
            <h2>Detected Objects:</h2>
           
                <ul>
                    <li v-for="object in detectedObjects" :key="object.class">
                    Object: {{ object.class }} || Score: {{ object.score }}
                    </li>
                </ul>
            
        </div>
    </div>

</template>
  
<script>
// @ is an alias to /src  
import UnderDeveloping from '@/components/UnderDeveloping.vue';
import axios from 'axios'

export default {
    name: 'ImageAnalysisView',
    components: {
        UnderDeveloping
    },
    data() {
        return {
            file: undefined,
            fileUrl: undefined,
            detectedObjects: [],
            imageUploaded: false,
            loading: false
        }
    },
    methods: {
        handleFileUpload() {
            this.file = this.$refs.file.files[0];
            this.imageUploaded = true;

            if (!this.file) {
                return;
            }

            this.fileUrl = (window.URL || window.webkitURL).createObjectURL(this.file);
            URL.revokeObjectURL(this.file)
        },
        submitFile() {
            let formData = new FormData();

            formData.append('file', this.file);
            this.loading = true;

            axios.post('/detect_objects', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            }).then(response => {
                const data = response.data;

                if (data.result == false) {
                    alert(response.message);
                    return;
                }

                this.detectedObjects = response.data;
                this.loading = false;

            }).catch(error => {
                console.error(error);
                this.loading = false;
            });

        },
        clear() {
            this.file = undefined;
            this.fileUrl = undefined;
            this.detectedObjects = [];
            this.imageUploaded = false;
            this.loading = false
        }

        
    }
}
</script>

<style>

@import '../../styles/buttons_styles.css';
@import '../../styles/loading_animation.css';
@import '../../styles/output_boxes_animations.css';

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

.detectedObjects {
    display: flex;
    flex-direction: column;
    align-items: center;
    height: 500px;
    width: 500px;
    background-color: rgb(30, 30, 30) !important;
    border: 2px solid rgb(255, 255, 255);
    padding: 1em;
    color: white;
}

.detectedObjects img {
    margin-top: 10px;
    margin-bottom: 10px;
    width: 100px;
    height: auto;
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