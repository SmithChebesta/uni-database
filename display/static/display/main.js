const sidenav_btn = $('#navbarSideButton')
const sidenav = $('#sidenav')
// const table = $('table')
// table.click((e) => {
//     target = $(e.target)
//     if (target.hasClass('btn-primary')) {
//         // Edit
//         // console.log($(target.parents('tr')[0]).children('td'));
//         $(target.parents('tr')[0]).children('td').each((i, elem) => {
//             elem = $(elem)
//             console.log(elem);

//         });

//     }
//     if (target.hasClass('btn-danger')) {
//         // Delete

//     }

// })

sidenav_btn.click(() => {
    switch (sidenav_btn.text().trim()) {
        case '<':
            sidenav_btn.text('>')
            sidenav.hide()
            break;

        case '>':
            sidenav_btn.text('<')
            sidenav.show()
            break;
    }

})
$(window).resize(function() {
    if ($(window).width() < 960) {
        sidenav_btn.text('>')
        sidenav.hide()
    } else {
        sidenav_btn.text('<')
        sidenav.show()
    }
});