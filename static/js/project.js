/* Project specific Javascript goes here. */


$(function() {
    $('tr').click( function() {
        var href = $(this).closest("tr").find("a").attr("href")
//        window.location = $(this).find('a').attr('href');
            if(href)
            {
                window.location = href;
            }
    }).hover( function() {
            $(this).toggleClass('hover');
        });
});

function deleteRow(pp_id)  
{   
    var row = document.getElementById(pp_id).parentElement.parentElement;
    row.parentNode.removeChild(row);
}