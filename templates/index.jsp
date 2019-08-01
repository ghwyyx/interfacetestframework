<!DOCTYPE html>
<html>
<head>
<title>请求</title>
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
<div class="seconddiv" >
	<form method="post" action="">
		<div class="inputtypeclass">
			<label class="requestlabel"><span style="color:red; margin-right:10px;">* </span>请求类型:</label>
			<select id = "mySelect" onchange="displayResult()" name="requestselect">
				<option value="GET">GET</option>
				<option value="POST">POST</option>
			</select>
		</div>
		
		<div class="urlclass">
			<label class="urlspan"><span style="color:red; margin-right:10px;">* </span>URL地址:</label>
			<input class="urlinput" placeholder="请输入请求接口地址" name="requestsurl" required>
		</div>
		
		<div class="bodyclass">
			<label class="bodyspan"><span style="color:red; margin-right:10px;">* </span>body:</label>
			<textarea class="textareaclass" placeholder="请输入body数据" name="requestvalue"></textarea>
		</div>
		
		<div class="exceptclass">
			<span class="exceptspan">预期返回参数个数:</span>
			<input class="exceptinput" placeholder="预期返回参数个数" name="input_number">
		</div>
		<div class="saveclass">
            <input class="saveinput" name="saveinput" type="checkbox" >存储该接口作为回归测试接口
        </div>
		<div class="sendclass">
			<button type="submit" class="sendbutton">发送</button>
		</div>
	</form>
</div>
</body>
</html>