$(function () {
  $("#comembre_cooperative_id").on("change", function () {
    comembre_cooperative_id = $(this).val();
    // alert(comembre_cooperative_id);
    $.get(
      "/credits/getmembre",
      {
        comembre_cooperative_id: comembre_cooperative_id,
      },
      function (data,textStatus,jqxHR) {
        $("#comembre_membre_id").html(data);
      }
    );
  });
});

// cotisations
$(function () {
  $("#comembre_cooperative_id").on("change", function () {
    comembre_cooperative_id = $(this).val();
    // alert(comembre_cooperative_id);
    $.get(
      "/cotisations/getmembre",
      {
        comembre_cooperative_id: comembre_cooperative_id,
      },
      function (data,textStatus,jqxHR) {
        $("#comembre_membre_id").html(data);
      }
    );
  });
});




$('#form-create').on('keyup', function () {
  var credit_membre_id = $(this).find('#credit_membre_id').val();
  var montant_remboursement = $('#montant_remboursement').val();
  var list = [credit_membre_id,montant_remboursement]
  // alert(montant_remboursement);
  $.get(
    "/remboursements/getremboursement",
    {
      credit_membre_id: credit_membre_id,
      montant_remboursement: montant_remboursement,
    },
    function (data) {
      $("#reste_credit").val(data);
    }
  );
});
