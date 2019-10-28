# url命令

```text
// 获取所有用户的信息
http://localhost:3000/users

// 获取id=1的信息
http://localhost:3000/users/1
http://localhost:3000/users?id=1

// 获取所有公司的信息
http://localhost:3000/companies

// 获取单个公司的信息
http://localhost:3000/companies/1
http://localhost:3000/companies?id=1

// 获取公司id=3的所有用户的信息
http://localhost:3000/companies/3/users

// 根据公司名字获取信息
http://localhost:3000/companies?name=Apple

// 根据多个名字获取公司信息
http://localhost:3000/companies?name=Apple&name=Microsoft

// 获取一页中只有两条数据
http://localhost:3000/companies?_page=1&_limit=2

// 升序/降序排序
http://localhost:3000/companies?_sort=name&_order=asc
http://localhost:3000/companies?_sort=name&_order=desc

// 获取年龄30以及30以上的数据
http://localhost:3000/users?age_gte=30

// 年龄30-40之间的数据
http://localhost:3000/users?age_gte=30&age_lte=40

// 搜索用户信息[关键字q=]
http://localhost:3000/users?q=Henry

```
