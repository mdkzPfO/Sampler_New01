$(function() {
  // 「#language-wrapper」にhoverしたときのhoverイベントを作成してください
  //"*まず、指定項目の値がhoverされると紐づいた画面が右側に表示され、そこからhoverが外れても何もしないようにする
  $("a").hover(
    function(){
      $(this).css("color","red");
    },
    function(){
      $(this).css("color","");
  });
 //**そして、Function_ListBoxエリアがhoverされると何も行わず、抜けたときだけfadeOutさせる
  $(".Function_ListBox").hover(
    function(){
    },
    function(){
      $(name).stop().fadeOut(1);
      $(".Function_List_HiddenFrame").css("opacity","0");
      $(".Function_List_HiddenFrame").css("z-index","-1");
  });
  $(".Function_List a").hover(
    function(){
      if ($(this).hasClass("Sampling")){
        if (typeof name !== 'undefined' && name !==".Sampling_HiddenFrame" ) {
          $(name).stop().fadeOut(1);
        }
        $(".Function_List_HiddenFrame").css("opacity","1");
        $(".Function_List_HiddenFrame").css("z-index","100");
        name=".Sampling_HiddenFrame"
        $(name).fadeIn(1000);
      }
      else if ($(this).hasClass("Report")){
        if (typeof name !== 'undefined' && name !==".Report_HiddenFrame") {
          $(name).stop().fadeOut(1);
        }
        $(".Function_List_HiddenFrame").css("opacity","1");
        $(".Function_List_HiddenFrame").css("z-index","100");

        name=".Report_HiddenFrame"
        $(name).fadeIn(1000);
      }
      else if ($(this).hasClass("Animal")){
        if (typeof name !== 'undefined' && name !==".Animal_HiddenFrame") {
          $(name).stop().fadeOut(1);
        }
        $(".Function_List_HiddenFrame").css("opacity","1");
        $(".Function_List_HiddenFrame").css("z-index","100");
        name=".Animal_HiddenFrame"
        $(name).fadeIn(1000);
      } else {
        if (typeof name !== 'undefined' && name !==".Report_HiddenFrame") {
          $(name).stop().fadeOut(1);
        }
      }
    },
    function(){


  });
  $(".User_Search_name").hover(
    function(){
      $(this).find(".User_Search_action_name").fadeIn(1);
      console.log("わっしょい");
    },
    function(){
      $(this).find(".User_Search_action_name").fadeOut(1);
    }
  );
  $(".Table_Action_List").hover(
    function(){
      $(this).find("#Action_ID").show();
    },
    function(){
      $(this).find("#Action_ID").hide();

    }
  );
  $("#Experiment_Add").click(function(){
    var ironna_tag = $('.Group_SituationFrame_Box').children().length+1;
    var GR_form=''+
    '<div class="Group_SituationFrame">'+
    '<div class="Group_Title"><p>グループ名 &nbsp&nbsp&nbsp&nbsp&nbsp:<input type="text" required=False name=group_name0' + ironna_tag + ' ></p><p>&nbsp&nbsp&nbsp&nbsp&nbspN数:<input class="Number_Input_Box" required=False type="text" name=experiment_number0'+ ironna_tag + '></p></div>'+
    '<div class="Group_Situation"><p>実験条件&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp:</p><textarea type="text" required=False name=experiment_situation0' + ironna_tag + ' class="Long_Input_Box"></textarea></div>'+
    '</div>';
    console.log(GR_form);
    var ironna_tag = $('.Group_SituationFrame_Box').children().length;
    console.log(ironna_tag);
    if ( ironna_tag == 6){
      $('.Group_SituationFrame_Box').append('<p>これ以上は追加できません</p>');

    } else if ( ironna_tag > 6){
      console.log("どっせーい")
    }
    else {
      $('.Group_SituationFrame_Box').append(GR_form);
      $('.hidden_number:first').remove();
      $('.hidden_group:first').remove();
      $('.hidden_situation:first').remove();
    }
  });
  $(".SamplingDetail_Action").hover(
    function(){
      $(".SamplingDetail_ActionList_Under").show();
    },
    function(){
      $(".SamplingDetail_ActionList_Under").hide();
    }

);
});
