<%--
  Created by IntelliJ IDEA.
  User: rytter
  Date: 2022/12/14
  Time: 下午9:40
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Title</title>
</head>
<body>
<form action="login" method="get">
    <div class="login_box">
        <legend class="title">系统登录</legend>
        <input class="input_box" type="text" name="name" placeholder="用户名">
        <input class="input_box" type="text" name="password" placeholder="密码">
        <input class="button_box" type="submit" name="btn" value="登录"><br /><br />
        <a class="link" href="SignUp.jsp">点击注册</a>
    </div>
</form>
</body>
</html>
