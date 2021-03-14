require(["esri/widgets/Sketch", "esri/Map", "esri/Graphic", "esri/layers/GraphicsLayer", "esri/views/MapView", "esri/symbols/TextSymbol"], function(
  Sketch,
  Map,
  Graphic,
  GraphicsLayer,
  MapView,
  TextSymbol
) {
  const layer = new GraphicsLayer()
  const map = new Map({
    basemap: "topo-vector",
    layers: [layer]
  })
    const request = new XMLHttpRequest();
    const url = "/api/arcgis/stations/";

    /* Здесь мы указываем параметры соединения с сервером, т.е. мы указываем метод соединения GET,
    а после запятой мы указываем путь к файлу на сервере который будет обрабатывать наш запрос. */
    request.open('GET', url);

    // Указываем заголовки для сервера, говорим что тип данных, - контент который мы хотим получить должен быть не закодирован.
    request.setRequestHeader('Content-Type', 'application/x-www-form-url');

    // Здесь мы получаем ответ от сервера на запрос, лучше сказать ждем ответ от сервера
    request.addEventListener("readystatechange", () => {

        if (request.readyState === 4 && request.status === 200) {
          var arr_from_json = JSON.parse( request.responseText );
          arr_from_json.forEach(function(element, index, array) {
              const point = {
                type: 'point',
                longitude: element['lon'],
                latitude: element['lat'],
              };

              const textSymbol = {
                type: "text",
                color: "white",
                haloColor: "black",
                haloSize: 1,
                lineHeight: 1.5,
                text: element['IAGA'],
                yoffset: "5px",
              };

              const simpleMarkerSymbol = {
                  type: "simple-marker",  // autocasts as new SimpleMarkerSymbol()
                  style: "square",
                  color: [ 47, 102, 122, 0.7],
                  size: "4px",  // pixels
              };

              const pointGraphic = new Graphic({
                geometry: point,
                symbol: simpleMarkerSymbol
              });

              const textGraphic = new Graphic({
                geometry: point,
                symbol: textSymbol
              });

              layer.add(pointGraphic);
              layer.add(textGraphic);
          });

        }
    });

    // Выполняем запрос
    request.send();

  const view = new MapView({
    container: "viewDiv",
    map: map,
    zoom: 5,
    center: [90, 45]
  })

  const sketch = new Sketch({
    layer: layer,
    view: view,
    creationMode: "update"
  })
  view.ui.add(sketch, "top-right");
});
