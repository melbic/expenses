/* Project specific Javascript goes here. */


$(function () {
    $('tr').click(function () {
        var href = $(this).closest("tr").find("a").attr("href")
//        window.location = $(this).find('a').attr('href');
        if (href) {
            window.location = href;
        }
    }).hover(function () {
            $(this).toggleClass('hover');
        });

    // function sum_it(the_class) {
//         var total = 0;
// 		column = $(this).siblings(the_class).andSelf().index(this);
//         $(this).html(total);
//     }

function tally (selector) 
   {
     $(selector).each(function () 
     {
         var total = 0,
         column = $(this).siblings(selector).andSelf().index(this);
         $(this).parents().prevUntil(':has(' + selector + ')').each(function () 
         {
           total += parseFloat($('td.amount:eq(' + column + ')', this).html()) || 0;
         })
         $(this).html(total);
    });
   }
    tally('td.total');
});

function deleteRow(pp_id) {
    var row = document.getElementById(pp_id).parentElement.parentElement;
    row.parentNode.removeChild(row);
}