$(document).ready(function() {

    var $lang = $("select[name='lang']"),
        $resp = $("textarea[name='resp']"),
        $method = $("select[name='method']"),
        $preview = $("#preview"),
        $myTab = $("#myTab"),
        $previewSwitch = $("a[href='#preview']");


    function collect_param () {
        var user_params = {};
        $(".param").each(function(i, el) {
            var $el = $(el);
            var name = $.trim($el.find(".name").val());
            var type = $.trim($el.find(".type option:selected").val());
            if (name && type) {
                user_params[name] = type;
            }
        });
        str_params = JSON.stringify(user_params, null, 2);

        return {
            method: $method.val(),
            params: str_params,
            resp: $resp.val(),
            lang: $lang.val()
        };
    }

    function show_preview () {
        $previewSwitch.tab("show");
    }

    function update_preview () {
        $.get("/preview", collect_param(), function(res) {
            $preview.find("p").text(res);
        });
    }

    $(".add button").click(function() {
        var $params = $("#params");
        $params.append('<li class="param input-append input-prepend"><span class="add-on">name</span><input type="text" class="name"/><select class="type"><option>int</option><option selected>string</option></select></li>');
        return false;
    });

    $("form").submit(function() {
        var str_params = collect_param().params;
        $("input[type='hidden']").val(str_params);
    });

    $resp.on("keyup focusin", update_preview);
    $lang.on("change", update_preview);
    $("#params").on("change", ".name, .type", update_preview);

    $resp.focusin(function() {
        show_preview();
    });
    $("#params").on("focusin", ".name", function() {
        show_preview();
    });
    $lang.change(show_preview);

    set_indent($resp);

    $myTab.find('a').click(function (e) {
        $(this).tab('show');
        return false;
    });

    $(".syntax-helper").click(function() {
        var lang = $lang.val();
        $myTab.find("a[href='#" + lang + "']").tab("show");
    });
});
