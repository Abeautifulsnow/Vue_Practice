<template>
    <div class="details container">
        <router-link to="/" class="btn btn-default">返回</router-link>
        <h1 class="page-header">
            {{customer.name}}
            <span class="pull-right">
                <router-link :to="'/edit/'+customer.id" class="btn btn-primary">编辑</router-link>
                <button class="btn btn-danger" @click="deleteCustomer(customer.id)">删除</button>
            </span>
        </h1>
        <ul class="list-group">
            <li class="list-group-item"><span class="glyphicon glyphicon-phone-alt">&nbsp;{{customer.phone}}</span></li>
            <li class="list-group-item"><span class="glyphicon glyphicon-envelope">&nbsp;{{customer.email}}</span></li>
        </ul>
        <ul class="list-group">
            <li class="list-group-item">
                <span class="glyphicon glyphicon-education">&nbsp;{{customer.diploma}}</span>
            </li>
            <li class="list-group-item">
                <span class="glyphicon glyphicon-object-align-bottom">&nbsp;{{customer.graduation_school}}</span>
            </li>
            <li class="list-group-item">
                <span class="glyphicon glyphicon-headphones">&nbsp;{{customer.profession}}</span>
            </li>
            <li class="list-group-item">
                <span class="glyphicon glyphicon-user">&nbsp;{{customer.profile}}</span>
            </li>
        </ul>
    </div>
</template>

<script>

    export default {
        name: "CustomerDetails",
        data(){
            return {
                customer:"",
            }
        },
        methods: {
            fetchCustomers(id) {
                this.$http.get("http://localhost:3000/users/"+id)
                        .then(function (response) {
                            console.log(response);
                            this.customer = response.body;
                        })
            },
            deleteCustomer(id) {
                // alert(id);
                this.$http.delete("http://localhost:3000/users/"+id)
                        .then(function (response) {
                            this.$router.push({path:"/", query:{alert: "用户删除成功！"}});
                        })
            }
        },
        created() {
            this.fetchCustomers(this.$route.params.id);
        }
    }
</script>

<style scoped>

</style>