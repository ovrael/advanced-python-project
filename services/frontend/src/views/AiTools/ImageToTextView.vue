<template>
    <UnderDeveloping site-name=""></UnderDeveloping>
    <div id="file-upload-list" class="container">
        <div class="large-12 medium-12 small-12 cell">
            <label>File
                <input type="file" id="file" ref="file" v-on:change="handleFileUpload()" />
            </label>
            <button v-on:click="submitFile()">Submit</button>
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
            file: ''
        }
    },
    methods: {
        /*
            Submits the file to the server
        */
        submitFile() {
            /*
                    Initialize the form data
                */
            let formData = new FormData();

            /*
                Add the form data we need to submit
            */
            formData.append('file', this.file);

            /*
            Make the request to the POST /single-file URL
            */
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

        /*
            Handles a change on the file upload
        */
        handleFileUpload() {
            this.file = this.$refs.file.files[0];
        }
    }
}
</script>