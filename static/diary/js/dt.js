// flatpickrの実装方法
// https://noauto-nolife.com/post/flatpickr-install/

window.addEventListener("load" , function (){ 

  let config_date = { 
      locale: "ja"
  }   
//   config_dateオブジェクトのプロパティとして、locale: "ja"が設定されてる。localeプロパティは、Flatpickrの表示言語を指定している。この設定によりFlatpickrのUIや表示されるテキストが日本語になる。

  flatpickr("#date", config_date);
//   flatpickrを読み込むことで、flatpickr()関数をJS内で実行させることができる。第一引数は要素名、第二引数は設定。

});

// このコードは、指定された要素にFlatpickrを適用するための初期化処理を行っています。
// flatpickr()関数は、指定された要素に対してFlatpickrを適用するためのメソッドです。この例では、#dateというIDを持つ要素にFlatpickrが適用されます。つまり、その要素が日付選択用のカレンダーコンポーネントとなります。
// 引数としては、初期化のための設定オブジェクトであるconfig_dateが渡されています。このオブジェクトは、Flatpickrの動作をカスタマイズするためのプロパティを持っています。
// この初期化処理によって、指定された要素がFlatpickrのカレンダーコンポーネントに変わり、日付の選択や表示が行えるようになります。