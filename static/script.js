$(function() {
  // 「#language-wrapper」にhoverしたときのhoverイベントを作成してください
  //"*まず、指定項目の値がhoverされると紐づいた画面が右側に表示され、そこからhoverが外れても何もしないようにする
  $("a").hover(
    function(){
      $(this).css("color","red");

    },
    function(){
      $(this).css("color","white")
  });
 //**そして、Function_ListBoxエリアがhoverされると何も行わず、抜けたときだけfadeOutさせる
  $(".Function_ListBox").hover(
    function(){
    },
    function(){
      $(name).stop().fadeOut(1);
      $(".Function_List_HiddenFrame").css("opacity","0")
  });
  $(".Function_List a").hover(
    function(){
      $(this).css("color","grey");
      if ($(this).hasClass("Sampling")){
        if (typeof name !== 'undefined' && name !==".Sampling_HiddenFrame" ) {
          $(name).stop().fadeOut(1);
        }
        $(".Function_List_HiddenFrame").css("opacity","1")
        $(".Function_List_HiddenFrame").css("z-index","100")
        name=".Sampling_HiddenFrame"
        $(name).fadeIn(1000);
        $(this).css("color","purple");
      }
      else if ($(this).hasClass("Report")){
        if (typeof name !== 'undefined' && name !==".Report_HiddenFrame") {
          $(name).stop().fadeOut(1);
        }
        $(".Function_List_HiddenFrame").css("opacity","1")
          $(this).css("color","yellow");

        name=".Report_HiddenFrame"
        $(name).fadeIn(1000);
        $(this).css("color","yellow");
      }
      else if ($(this).hasClass("Animal")){
        if (typeof name !== 'undefined' && name !==".Animal_HiddenFrame") {
          $(name).stop().fadeOut(1);
        }
        $(".Function_List_HiddenFrame").css("opacity","1")
        name=".Animal_HiddenFrame"
        $(name).fadeIn(1000);
        $(this).css("color","pink");

      } else {
        if (typeof name !== 'undefined' && name !==".Report_HiddenFrame") {
          $(name).stop().fadeOut(1);
        }
      }
    },
    function(){


  });
  $(".container_action").hover(
    function(){
      $(this).find(".container_action_name").fadeIn(1);
    },
    function(){
      $(this).find(".container_action_name").fadeOut(1);
    }
  );

});
