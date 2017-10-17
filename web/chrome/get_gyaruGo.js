$(function(){

	console.log("--- START2 ---------------------------------");
	console.log($category)
	console.log($url)

	var x = document.getElementsByClassName("fontMiddiumText")[0].getElementsByTagName("p");

	console.log(x);

		for(var i = 0; i < x.length; ++i){

		console.log("   x[i].innerHTML をAPIに投げる");
		var beforeText = x[i].innerHTML;


		(function() {
			$.ajaxSetup({ async: false }); // 同期させる

			$.ajax({
//				url: 'https://pyladiesmockapi.azurewebsites.net/api/HttpTriggerJS2?code=o7xXgHNvxaTVQTRdC3KLUWcLR4TCwAcILxRgNpFu1rnUNGJWsFoUAw==',
				url: 'http://52.191.161.187:8888/world/replace',
			type:'POST',
			dataType: 'json',
			data: {
	  		"text" : beforeText
			},
			success: function(data) {
				console.log("データ取得：ok");

				$.each(data, function(key, value) {
					if (key == "replaceText") {
						var replaceText =  value;
						console.log("   APIから返ってきたテキストを x[i].innerHTML に渡す（本番）");
						console.log(replaceText);
						$afterText = replaceText;
						}

						if (key == "category") {
						$category =  value;
						}else if (key == "url") {
						$url =  value;
						}
					});

		},
			error: function(XMLHttpRequest, textStatus, errorThrown) {
				console.log("データ取得：ng");
			}
	  });
		x[i].innerHTML = $afterText;
		console.log($afterText)

		$.ajaxSetup({ async: true }); // 非同期に戻す

	}());




		}


	console.log("--- END2 -----------------------------------");
});
