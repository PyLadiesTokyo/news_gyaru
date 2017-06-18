$(function(){

	console.log("--- START1 ---------------------------------");
	var href = window.location.href ;
	console.log(href);

	(function() {
		$.ajaxSetup({ async: false }); // 同期させる

		$.ajax({
		url: 'https://pyladiesmockapi.azurewebsites.net/api/HttpTriggerJS1?code=bDF0uMuk9e/xKcInVcny8/x9GjUb0aGM1ulmiUz8nBQdRZTz4X9DyQ==',
		url: 'http://52.191.161.187:8888/url',
		type:'POST',
		dataType: 'json',
		data: {
  		"url" : href
		},
		success: function(data) {
			console.log("データ取得：ok");

			$.each(data, function(key, value) {
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
	console.log($category)
	console.log($url)

	$.ajaxSetup({ async: true }); // 非同期に戻す

}());

console.log("--- END1 ---------------------------------");
});
