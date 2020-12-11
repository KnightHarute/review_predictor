<template>
    <div>
        <el-container>
            <el-header></el-header>
            <el-main>
                <el-row type="flex" justify="center">
                    <el-col :span="12" style="text-align: center">
                        <span style="font-size: 52px"><strong>Review Rating Predictor v2.0</strong></span>
                    </el-col>
                </el-row>

                <el-row type="flex" justify="center">
                    <el-col :span="12" style="text-align: center">
                        <span style="font-size: 32px">Powered by <strong>Linear Support Vector Regression</strong></span>
                    </el-col>
                </el-row>

                <el-row type="flex" justify="center">
                    <el-col :span="12" style="text-align: center">
                        <span style="font-size: 24px"><strong>Now support for All kinds of business</strong></span>
                    </el-col>
                </el-row>
                <el-row type="flex" justify="center">
                    <el-col :span="12" style="text-align: center">
                        <span style="font-size: 20px">No Need for Selecting Category</span>
                    </el-col>
                </el-row>

                <el-row type="flex" justify="center" style="margin-top: 15px">
                    <el-col :span="12">
                        <el-form ref="form" :model="form" label-width="80px">
<!--                            <el-form-item label="category:">-->
<!--                                <el-input v-model="form.category"></el-input>-->
<!--                            </el-form-item>-->

                            <el-form-item label="Review:">
                                <el-input autosize type="textarea" v-model="form.review"></el-input>
                            </el-form-item>

                            <el-form-item v-if="status" label="Rating:">
                               <strong>{{form.rating}}</strong>
                            </el-form-item>

                            <el-form-item style="text-align: center">
                                <el-button style="margin-left: -20px" type="primary" @click="onsubmit">submit
                                </el-button>
                                <el-button type="info" @click="clear">clear</el-button>
                            </el-form-item>
                        </el-form>
                    </el-col>
                </el-row>
            </el-main>
        </el-container>
    </div>
</template>

<script>
    import axios from 'axios';//this.axios

    export default {
        name: 'app',
        components: {},
        data() {
            return {
                form: {
                    // category: '',
                    review: '',
                    rating: ''
                },
                status: false

            }
        },
        methods: {
            handleSelect(key, keyPath) {
                console.log(key, keyPath);
            },

            onsubmit() {

                //if(this.form.category==='' || this.form.review==='' ){
                if(this.form.review===''){
                    this.$message('input cannot be empty');
                    return false;
                }


                axios({
                    method: 'post',
                    url: 'http://149.28.91.13:5000/sub',
                    // url: 'sub',

                    data: {
                        // "category":this.form.category,
                        "review":this.form.review
                    }
                }).then(res => {
                        this.status = true;
                        this.form.rating =res.data;
                }).catch((error) => {
                    if(error.response.status === 500) {
                        console.log(error.response.data);
                        console.log(error.response.status);
                        console.log(error.response.headers);

                        this.$message('Connection failed. Error code:500');

                    }
                })


            },

            clear() {
                this.status = false;
                this.form = {
                    // category: '',
                    review: '',
                    rating: ''
                }
            }
        },


    }
</script>

<style>

</style>
