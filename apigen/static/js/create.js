$(document).ready(function() {
	$(".add button").click(function() {
		var $params = $("#params");
		$params.append('<li class="param input-append input-prepend"><span class="add-on">name</span><input type="text" class="name"/><select class="type"><option>int</option><option selected>string</option></select></li>');
		return false;
	});

	$("form").submit(function() {
		var params = [];
		$(".param").each(function(i, el) {
			var $el = $(el);
			var name = $.trim($el.find(".name").val());
			var type = $.trim($el.find(".type option:selected").val());
			if (name && type) {
				params.push(name+":"+type);
			}
		});
		var str_params = params.join(",");
		$("input[type='hidden']").val(str_params);
	});
});
