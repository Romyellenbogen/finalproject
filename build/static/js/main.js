$(document).ready(() =>{

  $('.sitebody').hide();

  $('.sitename').on('click', event => {
    $(event.currentTarget).next().slideToggle('.sitebody');
  })

  $('.culturebody').hide();

  $('.culturename').on('click', event => {
    $(event.currentTarget).next().slideToggle('.culturebody');
  })

  $('.culturename').click(function () {
    $(this).css({'color': '#843539', 'font-weight': 'bold'})
  });

  $('.sitename').click(function () {
    $(this).css({'color': '#843539', 'font-weight': 'bold'})
  });


})
