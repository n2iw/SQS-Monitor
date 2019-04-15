
$(window).on('load', function(){
    function queryStatus() {
        const product = $('#product').val();
        const tier = $('#tier').val();
        $('#avl-msg').text('');
        $('#in-flt').text('');
        $.ajax('queryStatus').done(function(result){
            console.log(result);
            $('#avl-msg').text(result.avl);
            $('#in-flt').text(result.inflt);
        });
    }

    console.log("Page loaded!");

    $('#product').change(function(e){
        const product = $(e.target).val();
        console.log(product);
        queryStatus();
    });

    $('#tier').change(function(e){
        const tier = $(e.target).val();
        console.log(tier)
        queryStatus();
    });
});