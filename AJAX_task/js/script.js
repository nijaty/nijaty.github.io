
console.log("js ishleyir");

$(document).ready(function(e) {
    $("button").click(function(e) {
        console.log("click");
        $.ajax({
            url: "https://fake.munisisazade.com/v1/5cd1746dfd1d61e440b4ca48",
            method: "GET",
            contentType: "application/json",
            success: function(data) {
                $(".result").html(
                    data.name + " " + data.albumName + data.year
                )

            },
            error: function(xhr, err, msg) {
                console.log(xhr, err, msg);
            }
        })
    
    }); 
});