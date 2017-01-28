$('#likes').click(function(){
	console.log("test message")
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/mango/like_category/', {category_id: catid}, function(data){
               $('#like_count').html(data);
               $('#likes').hide();
    });
});

$('#suggestion').keyup(function(){
        var query;
        query = $(this).val();
        $.get('/mango/suggest_category/', {suggestion: query}, function(data){
         $('#cats').html(data);
        });
});
