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
    <div align="center"><br/>
        <fieldset style="='width:80%">
            <legend>请填写您的登录信息</legend><br/>
            <div class="line">
                <div align="left" class="leftDiv">用户名</div>
                <div align="left" class="rightDiv">
                    <input type="text" name="name" class="text">
                </div>
            </div>
            <div class="line">
                <div align="left" class="leftDiv">密码</div>
                <div align="left" class="rightDiv">
                    <input type="text" name="password" class="text">
                </div>
            </div>
            <div class="line">
                <div align="left" class="rightDiv">
                    <br/><input type="submit" name="btn" value="提交" class="button"><br/>
                </div>
            </div>
        </fieldset>
    </div>
</form>
</body>
</html>
