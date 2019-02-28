<template>
    <div class="home">
      <!-- 第一行 -->
      <el-row display="margin-top:10px">
        <el-col :span="4"><el-input v-model="input" placeholder="请输入书名"></el-input></el-col>
        <el-button type="primary" @click="addBook()">新增</el-button>
      </el-row>
      <!-- 第二行 -->
      <el-row>
        <el-table :data="bookList" style="width: 100%" border>
          <el-table-column prop="id" label="编号" min-width="100">
            <template scope="scope"> {{ scope.row.pk }} </template>
          </el-table-column>
          <el-table-column prop="book_name" label="书名" min-width="100">
            <template scope="scope"> {{ scope.row.fields.book_name }} </template>
          </el-table-column>
          <el-table-column prop="add_time" label="添加时间" min-width="100">
            <template scope="scope"> {{ scope.row.fields.add_time }} </template>
          </el-table-column>
        </el-table>
      </el-row>
    </div>
</template>

<script>
    export default {
        name: "Library",
        data() {
          return {
            input: '',
            bookList: [],
          }
        },
        mounted: function() {
          this.showBooks()
        },
        methods: {
          addBook(){
            this.$http.get('http://127.0.0.1:8000/api/add_book?book_name=' + this.input)
              .then((response) => {
                var res = JSON.parse(response.bodyText)
                if (res.error_num == 0) {
                  this.showBooks()
                } else {
                  this.$message.error('新增书籍失败，请重试')
                  console.log(res['msg'])
                }
              })
          },
          showBooks() {
            this.$http.get('http://127.0.0.1:8000/api/show_books')
              .then((response) => {
                var res = JSON.parse(response.bodyText)
                console.log(res)
                if (res.error_num == 0) {
                  this.bookList = res['list']
                } else {
                  this.$message.error('查询书籍失败')
                  console.log(res['msg'])
                }
              })
          }
        }
    }
</script>

<style scoped>
h1, h2 {
  font-weight: normal;
}
  ul {
    list-style-type: none;
    padding: 0;
  }
  
  li {
    display: inline-block;
    margin: 0 10px;
  }
  
  a{
    color: #42b983;
  }
</style>
