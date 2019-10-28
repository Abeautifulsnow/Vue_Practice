<template>
    <div class="edit container">
        <Alert v-if="alert" :message="alert"></Alert>
        <h1 class="page-header">编辑用户</h1>
        <form @submit="updateCustomer">
            <div class="well">
                <h4>用户信息</h4>
                <div class="form-group">
                    <label for="name">姓名</label>
                    <input type="text" class="form-control" placeholder="name" v-model="customer.name">
                </div>
                <div class="form-group">
                    <label for="phone">电话</label>
                    <input type="text" class="form-control" placeholder="phone" v-model="customer.phone">
                </div>
                <div class="form-group">
                    <label for="email">邮箱</label>
                    <input type="text" class="form-control" placeholder="email" v-model="customer.email">
                </div>
                <div class="form-group">
                    <label for="diploma">学历</label>
                    <input type="text" class="form-control" placeholder="diploma" v-model="customer.diploma">
                </div>
                <div class="form-group">
                    <label for="graduation_school">毕业学校</label>
                    <input type="text" class="form-control" placeholder="graduation_school"
                           v-model="customer.graduation_school">
                </div>
                <div class="form-group">
                    <label for="profession">职业</label>
                    <input type="text" class="form-control" placeholder="profession" v-model="customer.profession">
                </div>
                <div class="form-group">
                    <label for="profile">个人简介</label>
                    <!--                    <input type="text" class="form-control" placeholder="profile" v-model="customer.profile">-->
                    <textarea class="form-control" name="profile" rows="10" v-model="customer.profile"></textarea>
                </div>
                <!-- submit绑定上面@submit后面的函数 -->
                <button class="btn btn-primary" type="submit">确认</button>
            </div>
        </form>
    </div>
</template>

<script>
    import Alert from "./Alert";
    export default {
        name: "Edit",
        data (){
            return {
                customer: {},
                alert: ""
            }
        },
        methods: {
            fetchCustomer(id){
                this.$http.get("http://localhost:3000/users/"+id)
                        .then(function (response) {
                            // console.log(response);
                            this.customer = response.body;
                        })
            },
            updateCustomer(e) {
                // 取消事件的默认动作
                // console.log(123);
                if (!this.customer.name || !this.customer.phone || !this.customer.email) {
                    // alert("请添加对应的信息！")
                    this.alert = "请添加对应的信息！";
                }else {
                    let updateCustomer = {
                        name: this.customer.name,
                        phone: this.customer.phone,
                        email: this.customer.email,
                        diploma: this.customer.diploma,
                        graduation_school: this.customer.graduation_school,
                        profession: this.customer.profession,
                        profile: this.customer.profile,
                    };

                    this.$http.put("http://127.0.0.1:3000/users/"+this.$route.params.id, updateCustomer)
                            .then(function (response) {
                                this.$router.push({path: "/", query: {alert: "用户信息更新成功！"}});
                            });
                    e.preventDefault();
                }
                // 阻止默认事件
                e.preventDefault();
            }
        },
        created() {
            // 给methods中fetchCustomer函数传递id值。
            this.fetchCustomer(this.$route.params.id)
        },
        components: {
            Alert
        }
    }
</script>

<style scoped>

</style>