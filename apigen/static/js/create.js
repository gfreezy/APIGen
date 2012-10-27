$(document).ready(function() {
	$(".add button").click(function() {
		var $params = $("#params");
		$params.append('<li class="param"><label>name</label><input type="text" class="name"/><label>type</label><input type="text" class="type"/></li>');
		return false;
	});

	$("form").submit(function() {
		var params = [];
		$(".param").each(function(i, el) {
			var $el = $(el);
			var name = $.trim($el.find(".name").val());
			var type = $.trim($el.find(".type").val());
			if (name && type) {
				params.push(name+":"+type);
			}
		});
		var str_params = params.join(",");
		$("input[type='hidden']").val(str_params);
	});
});
