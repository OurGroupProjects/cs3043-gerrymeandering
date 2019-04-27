const numCongress = 114;
let totalResults = [];


for (let currCongress = 1; currCongress <= numCongress; currCongress++) {
  d3.json("topo/districts" + currCongress.toString().padStart(3,'0') + ".json", doShit);
}

let textFile = null,
    makeTextFile = function (dataString) {
      let data = new Blob([dataString], {type: 'text/plain'});
      if (textFile !== null) {
        window.URL.revokeObjectURL(textFile);
      }

      textFile = window.URL.createObjectURL(data);
      return textFile;
    };
document.getElementById("fuk").addEventListener('click', () => {
  let link = document.getElementById("downloadLink");
  link.href = makeTextFile(totalResults);
  link.style.display = 'block';
}, false);

function doShit(congress) {

  let projection = d3.geo.albersUsa();
  let path = d3.geo.path()
      .projection(projection);


  let district_features = topojson.feature(congress, congress.objects[Object.keys(congress.objects)[0]]).features;

  let districtResults = get_data(district_features, 0);
  let dataString = JSON.stringify(districtResults);

  totalResults.push(dataString);



  function get_data(features, is_state) {

    let results = [];
    let maxFromCenter = 0;
    let perimeter = 0;


    features.forEach(function (d) {
      let area = path.area(d);
      if (!d.geometry) {
        return;
      }
      if (d.geometry.type == 'MultiPolygon') {
        let vals = multiPerimeter(d);
        perimeter = vals[0];
        maxFromCenter = vals[1];
      } else {
        let vals = featurePerimeter(d);
        perimeter = vals[0];
        maxFromCenter = vals[1];
      }

      entry = {
        computedStats: {area: area, perimeter: perimeter, maxFromCenter: maxFromCenter},
        properties: d.properties
      };
      console.log(d.properties.STARTCONG);
      results.push(entry)
    });

    return results
  }

  function multiPerimeter(feature) {
    let perimeter = 0;
    let maxDistance = 0;
    let coordinateSet = feature.geometry.coordinates;
    let centerPoint = path.centroid(feature);

    coordinateSet.forEach(function (c) {
      let coordinates = c[0];
      let points = coordinates.length;
      let partialP = 0;
      let partialMax = getMaxFromCenter(centerPoint, coordinates);

      for (let i = 0; i < points; i++) {
        if (i != points - 1) {
          l = d3.geo.distance(coordinates[i], coordinates[i + 1])
        } else {
          l = d3.geo.distance(coordinates[i], coordinates[0])
        }
        partialP += l
      }
      if (partialMax >= maxDistance) {
        maxDistance = partialMax;
      }
      perimeter += partialP
    })
    return [perimeter, maxDistance]
  }

  function featurePerimeter(feature) {
    let coordinates = feature.geometry.coordinates[0];
    let points = coordinates.length;
    let centerPoint = path.centroid(feature);
    let maxDistance = getMaxFromCenter(centerPoint, coordinates);
    let perimeter = 0;

    for (let i = 0; i < points; i++) {
      if (i != points - 1) {
        l = d3.geo.distance(coordinates[i], coordinates[i + 1])
      } else {
        l = d3.geo.distance(coordinates[i], coordinates[0])
      }
      perimeter += l
    }
    return [perimeter, maxDistance]
  }

  function getMaxFromCenter(center, coordinates) {
    let l = 0;
    coordinates.forEach(function (c) {
      nl = d3.geo.distance(c, center);
      if (nl >= l) {
        l = nl;
      }
    });
    return l;
  }
}

