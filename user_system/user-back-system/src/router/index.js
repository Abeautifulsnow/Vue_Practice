import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Customers from "../components/Customers";
import About from "../components/About";
import Add from "../components/Add"
import CustomerDetails from "../components/CustomerDetails";
import Edit from "../components/Edit";

Vue.use(Router)

// 设置路由
// const router = new Router({
//     mode: "history",
//     base: __dirname,
//     routes: [
//         {path: "/", component: Customers},
//         {path: "/about", component: About}
//     ]
// })

export default new Router({
    mode: "history",
    base: __dirname,
    routes: [
        {path: "/", component: Customers},
        {path: "/about", component: About},
        {path: "/add", component: Add},
        {path: "/customer/:id", component: CustomerDetails},
        {path: "/edit/:id", component: Edit}
    ]
})
