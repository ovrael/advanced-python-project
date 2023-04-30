<template>
    <UnderDeveloping site-name=""></UnderDeveloping>

    <div class="imageUpload container text-center">
        <div class="imagePlaceholder" :class="{ 'imagePlaceholderSquare': !file }">
            <div v-if="!file" class="imageUploadLabel">
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
                    <button v-on:click="() => { this.file = undefined }" class="btn btn-danger text-center w-100" type="button">Clear 💀</button>
                </div>

                <div class="col-md-3 col-sm-12 offset-md-6 px-0 mt-4">
                    <button v-on:click="submitFile()" class="btn btn-success text-center  w-100" type="button">Submit ➣</button>
                </div>

            </div>

        </div>
    </div>
</template>
  
<script>
// @ is an alias to /src  
import UnderDeveloping from '@/components/UnderDeveloping.vue';
import axios from 'axios'

export default {
    name: 'ImageToTextView',
    components: {
        UnderDeveloping
    },
    data() {
        return {
            file: undefined,
            fileUrl: null,
        }
    },
    methods: {
        submitFile() {
            let formData = new FormData();

            formData.append('file', this.file);

            axios.post('/uploadfile', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            }).then(response => {
                const data = response.data;

                if (data.result == false) {
                    console.warn(response.message);
                    return;
                }

                console.log(data);

            }).catch(error => {
                console.error(error);
            });

        },

        handleFileUpload() {
            this.file = this.$refs.file.files[0];
            if (this.file === undefined)
                return;

            this.fileUrl = (window.URL || window.webkitURL).createObjectURL(this.file);
            URL.revokeObjectURL(this.file)
        }
    }
}
</script>

<style>
.imageUpload {
    margin: 0 auto;
    margin-top: 15%;
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