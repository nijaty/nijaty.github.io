
console.log("js ishleyir");

$(document).ready(function(e) {
    $("button").click(function(e) {
        console.log("click");
        $.ajax({
            url: "https://fake.munisisazade.com/v1/5cd8c0b2fd1d61e440b4d192",
            method: "GET",
            contentType: "application/json",
            success: function(data) {
                console.log(data);
                $(data).each(function(index, value){
                    var record="<tr><td>"+value.name+"</td><td>"+value.albumName+"</td><td>"+value.year+"</td></tr>";
                    $("table").append(record);
                });
                    
            }  
           
        });
    
    }); 
});
