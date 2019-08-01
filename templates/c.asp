<!DOCTYPE html>
<html>
<head>
<title>结果</title>
<link rel="stylesheet" href="../static/css/1.css">
<script type="text/script" src="../static/js/common/jquery-3.4.1.min.js"></script>
<script type="text/script" scr="../static/js/private/1.js"></script>
</head>

<body>
<div id="navone">
<ul id="ulone">
<li id="lione"><a href="./a.asp">请求</a></li>
<li id="lione"><a href="./b.asp">接口列表</a></li>
<li id="lione"><a href="./c.asp">请求结果</a></li>
</ul>
</div>
<div class="resultclass">
	<textarea class="resultdata" placeholder="暂无数据" name="responseresult" onchange="showresult()" readonly="readonly">{{result}}</textarea>
</div>
</body>
</html>
