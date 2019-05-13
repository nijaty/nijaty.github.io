$(document).ready(function(e) {
    $("button").one('click', function(e) {
        $.ajax({
            url: "https://fake.munisisazade.com/v1/5cd8d428fd1d61e440b4d1dc",
            method: "GET",
            contentType: "application/json",
            success: function(data) {
                $(data).each(function(index, value){
                    var record="<tr><td>"+value.artistName+"</td><td>"+value.albumName+"</td><td>"+value.albumYear+"</td></tr>";
                    $("table").append(record);
                });
                    
            }  
           
        });
    
    }); 
});
