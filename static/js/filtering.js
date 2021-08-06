$(document).ready(function(){
    $(".nese").on('click',function(){
        var _filterObj = {};
        $(".nese").each(function(index,ele){
            var _filterVal = $(this).val();
            var _filterKey = $(this).data('filter');
            console.log(_filterKey,_filterVal);
        });
    });
});