

// frappe.ui.form.on('Material Request',  {
//     validate: function(frm) {
//           msgprint('Hi, My Name Is Emad');
//
//          }
// });



frappe.ui.form.on('Material Request', {
    validate: function(frm) {
        $.each(frm.doc.items, function(i, d) {
          d.department = frm.doc.requested_department;
            if(d.department == ""){
              msgprint('Hi, My Name Is Emad')


            }

        });
    }
})
