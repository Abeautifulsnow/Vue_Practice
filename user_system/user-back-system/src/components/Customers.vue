<template>
    <div class="customers container">
        <Alert v-if="alert" v-bind:message="alert"></Alert>
        <h1 class="page-header">用户管理系统</h1>
        <input type="text" class="form-control" placeholder="搜索" v-model="filterInput">
        <br>
        <table class="table table-striped">
            <thead>
            <tr>
                <th>姓名</th>
                <th>电话</th>
                <th>邮箱</th>
                <th>详情</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="customer in filterBy(customers,filterInput)">
                <td>{{customer.name}}</td>
                <td>{{customer.phone}}</td>
                <td>{{customer.email}}</td>
                <td>
                    <router-link class="btn btn-default" v-bind:to="'/customer/'+customer.id">详情</router-link>
                </td>
            </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
    import Alert from './Alert'
    export default {
        name: 'Customers',
        data() {
            return {
                customers: [],
                alert:"",
                filterInput: ""
            }
        },
        methods: {
            fetchCustomers() {
                this.$http.get("http://localhost:3000/users")
                        .then(function (response) {
                            // console.log(response);
                            this.customers = response.body;
                        })
            },
            // 筛选匹配
            filterBy(customers,value){
                return customers.filter(function (customer) {
                    return customer.name.match(value);
                    // return customer.phone.match(value);
                })
            }
        },
        created() {
            if (this.$route.query.alert) {
                // 拿到全局路由中传入的alert对象数据，返回给上面default中的data()对象中的alert
                this.alert = this.$route.query.alert;
            }
            this.fetchCustomers();
        },
        // updated() {
        //     this.fetchCustomers();
        // },
        // 注册组件
        components: {
            Alert
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
