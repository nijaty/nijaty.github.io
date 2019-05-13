
console.log("js ishleyir");

$(document).ready(function(e) {
    $("button").click(function(e) {
        console.log("click");
        $.ajax({
            url: "https://fake.munisisazade.com/v1/5cd18ca5fd1d61e440b4cac9",
            method: "GET",
            contentType: "application/json",
            success: function(data) {
                console.log(data);
                $(".name").html(
                    data.name
                ),
                $(".albumName").html(
                    data.albumName
                ),

                $(".year").html(
                    data.year
                )
            }
           
        });
    
    }); 
});
