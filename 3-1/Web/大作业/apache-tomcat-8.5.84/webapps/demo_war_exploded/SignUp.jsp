<%--
 Created by IntelliJ IDEA.
 User: rytter Date: 2022/12/14 
 Time: 下午6:46 
 To change this template use File | Settings | File Templates. 
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>

<head>
    <link rel="stylesheet" href="style.css">
    <title>web安全作业（网盘）</title>
</head>

<body>
    <form action="signup" method="get">
        <div class="sign_box">
            <legend class="title">用户注册</legend>
            <input class="input_box" type="text" name="name" placeholder="用户名">
            <input class="input_box" type="text" name="password" placeholder="密码">
            <input class="input_box" type="text" name="confirm_code" placeholder="邀请码">
            <input class="button_box" type="submit" name="btn" value="注册">
        </div>
    </form>
</body>

</html>