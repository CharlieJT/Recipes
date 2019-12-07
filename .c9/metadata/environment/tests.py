{"filter":false,"title":"tests.py","tooltip":"/tests.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":55,"column":16},"end":{"row":55,"column":30},"action":"remove","lines":["Mac and cheese"],"id":278},{"start":{"row":55,"column":16},"end":{"row":55,"column":28},"action":"insert","lines":["Pumpkin rice"]}],[{"start":{"row":30,"column":26},"end":{"row":30,"column":27},"action":"remove","lines":["H"],"id":279}],[{"start":{"row":30,"column":26},"end":{"row":30,"column":27},"action":"insert","lines":["h"],"id":280}],[{"start":{"row":30,"column":31},"end":{"row":30,"column":32},"action":"remove","lines":["P"],"id":281}],[{"start":{"row":30,"column":31},"end":{"row":30,"column":32},"action":"insert","lines":["p"],"id":282}],[{"start":{"row":74,"column":4},"end":{"row":74,"column":5},"action":"remove","lines":[" "],"id":283}],[{"start":{"row":74,"column":4},"end":{"row":84,"column":43},"action":"insert","lines":["def test_delete_recipe(self):","        \"\"\"Delete recipe and check recipe is not present after redirect\"\"\"","        res = self.client.get('/recipes')","        # use regular expression to find Object id of recipe","        ids = re.findall(r'href=\"/recipe/(\\w+)\"', res.data.decode(\"utf-8\"))","        assert len(ids) > 0","        # togo that delete recipe page using extracted id","        res = self.client.post('/delete_recipe/{}'.format(ids[0]), follow_redirects=True)","        data = res.data.decode('utf-8')","        assert res.status == '200 OK'","        assert 'Mac and cheese' not in data"],"id":284}],[{"start":{"row":74,"column":33},"end":{"row":75,"column":0},"action":"insert","lines":["",""],"id":285},{"start":{"row":75,"column":0},"end":{"row":75,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":75,"column":8},"end":{"row":75,"column":74},"action":"insert","lines":["\"\"\"Delete recipe and check recipe is not present after redirect\"\"\""],"id":286}],[{"start":{"row":75,"column":11},"end":{"row":75,"column":71},"action":"remove","lines":["Delete recipe and check recipe is not present after redirect"],"id":287},{"start":{"row":75,"column":11},"end":{"row":75,"column":12},"action":"insert","lines":["T"]},{"start":{"row":75,"column":12},"end":{"row":75,"column":13},"action":"insert","lines":["e"]},{"start":{"row":75,"column":13},"end":{"row":75,"column":14},"action":"insert","lines":["s"]},{"start":{"row":75,"column":14},"end":{"row":75,"column":15},"action":"insert","lines":["t"]},{"start":{"row":75,"column":15},"end":{"row":75,"column":16},"action":"insert","lines":["i"]},{"start":{"row":75,"column":16},"end":{"row":75,"column":17},"action":"insert","lines":["n"]},{"start":{"row":75,"column":17},"end":{"row":75,"column":18},"action":"insert","lines":["g"]}],[{"start":{"row":75,"column":17},"end":{"row":75,"column":18},"action":"remove","lines":["g"],"id":288},{"start":{"row":75,"column":16},"end":{"row":75,"column":17},"action":"remove","lines":["n"]},{"start":{"row":75,"column":15},"end":{"row":75,"column":16},"action":"remove","lines":["i"]}],[{"start":{"row":75,"column":15},"end":{"row":75,"column":16},"action":"insert","lines":[" "],"id":289},{"start":{"row":75,"column":16},"end":{"row":75,"column":17},"action":"insert","lines":["d"]},{"start":{"row":75,"column":17},"end":{"row":75,"column":18},"action":"insert","lines":["e"]},{"start":{"row":75,"column":18},"end":{"row":75,"column":19},"action":"insert","lines":["l"]},{"start":{"row":75,"column":19},"end":{"row":75,"column":20},"action":"insert","lines":["e"]},{"start":{"row":75,"column":20},"end":{"row":75,"column":21},"action":"insert","lines":["t"]},{"start":{"row":75,"column":21},"end":{"row":75,"column":22},"action":"insert","lines":["e"]},{"start":{"row":75,"column":22},"end":{"row":75,"column":23},"action":"insert","lines":["i"]},{"start":{"row":75,"column":23},"end":{"row":75,"column":24},"action":"insert","lines":["n"]},{"start":{"row":75,"column":24},"end":{"row":75,"column":25},"action":"insert","lines":["g"]}],[{"start":{"row":75,"column":25},"end":{"row":75,"column":26},"action":"insert","lines":[" "],"id":290},{"start":{"row":75,"column":26},"end":{"row":75,"column":27},"action":"insert","lines":["a"]}],[{"start":{"row":75,"column":27},"end":{"row":75,"column":28},"action":"insert","lines":[" "],"id":291},{"start":{"row":75,"column":28},"end":{"row":75,"column":29},"action":"insert","lines":["r"]},{"start":{"row":75,"column":29},"end":{"row":75,"column":30},"action":"insert","lines":["e"]},{"start":{"row":75,"column":30},"end":{"row":75,"column":31},"action":"insert","lines":["c"]},{"start":{"row":75,"column":31},"end":{"row":75,"column":32},"action":"insert","lines":["i"]},{"start":{"row":75,"column":32},"end":{"row":75,"column":33},"action":"insert","lines":["p"]},{"start":{"row":75,"column":33},"end":{"row":75,"column":34},"action":"insert","lines":["e"]}],[{"start":{"row":75,"column":34},"end":{"row":75,"column":35},"action":"insert","lines":[" "],"id":292},{"start":{"row":75,"column":35},"end":{"row":75,"column":36},"action":"insert","lines":["a"]},{"start":{"row":75,"column":36},"end":{"row":75,"column":37},"action":"insert","lines":["n"]},{"start":{"row":75,"column":37},"end":{"row":75,"column":38},"action":"insert","lines":["d"]}],[{"start":{"row":75,"column":38},"end":{"row":75,"column":39},"action":"insert","lines":[" "],"id":293},{"start":{"row":75,"column":39},"end":{"row":75,"column":40},"action":"insert","lines":["r"]}],[{"start":{"row":75,"column":40},"end":{"row":75,"column":41},"action":"insert","lines":["c"],"id":294}],[{"start":{"row":75,"column":40},"end":{"row":75,"column":41},"action":"remove","lines":["c"],"id":295}],[{"start":{"row":75,"column":40},"end":{"row":75,"column":41},"action":"insert","lines":["e"],"id":296},{"start":{"row":75,"column":41},"end":{"row":75,"column":42},"action":"insert","lines":["c"]},{"start":{"row":75,"column":42},"end":{"row":75,"column":43},"action":"insert","lines":["i"]},{"start":{"row":75,"column":43},"end":{"row":75,"column":44},"action":"insert","lines":["p"]},{"start":{"row":75,"column":44},"end":{"row":75,"column":45},"action":"insert","lines":["e"]}],[{"start":{"row":75,"column":45},"end":{"row":75,"column":46},"action":"insert","lines":[" "],"id":297},{"start":{"row":75,"column":46},"end":{"row":75,"column":47},"action":"insert","lines":["i"]},{"start":{"row":75,"column":47},"end":{"row":75,"column":48},"action":"insert","lines":["s"]}],[{"start":{"row":75,"column":48},"end":{"row":75,"column":49},"action":"insert","lines":[" "],"id":298},{"start":{"row":75,"column":49},"end":{"row":75,"column":50},"action":"insert","lines":["n"]},{"start":{"row":75,"column":50},"end":{"row":75,"column":51},"action":"insert","lines":["o"]},{"start":{"row":75,"column":51},"end":{"row":75,"column":52},"action":"insert","lines":["t"]}],[{"start":{"row":75,"column":52},"end":{"row":75,"column":53},"action":"insert","lines":[" "],"id":299},{"start":{"row":75,"column":53},"end":{"row":75,"column":54},"action":"insert","lines":["f"]},{"start":{"row":75,"column":54},"end":{"row":75,"column":55},"action":"insert","lines":["o"]},{"start":{"row":75,"column":55},"end":{"row":75,"column":56},"action":"insert","lines":["u"]},{"start":{"row":75,"column":56},"end":{"row":75,"column":57},"action":"insert","lines":["n"]}],[{"start":{"row":75,"column":57},"end":{"row":75,"column":58},"action":"insert","lines":["d"],"id":300}],[{"start":{"row":75,"column":58},"end":{"row":75,"column":59},"action":"insert","lines":[" "],"id":301},{"start":{"row":75,"column":59},"end":{"row":75,"column":60},"action":"insert","lines":["a"]},{"start":{"row":75,"column":60},"end":{"row":75,"column":61},"action":"insert","lines":["f"]},{"start":{"row":75,"column":61},"end":{"row":75,"column":62},"action":"insert","lines":["t"]}],[{"start":{"row":75,"column":62},"end":{"row":75,"column":63},"action":"insert","lines":["e"],"id":302},{"start":{"row":75,"column":63},"end":{"row":75,"column":64},"action":"insert","lines":["r"]}],[{"start":{"row":75,"column":64},"end":{"row":75,"column":65},"action":"insert","lines":[" "],"id":303}],[{"start":{"row":75,"column":65},"end":{"row":75,"column":66},"action":"insert","lines":["p"],"id":304},{"start":{"row":75,"column":66},"end":{"row":75,"column":67},"action":"insert","lines":["a"]},{"start":{"row":75,"column":67},"end":{"row":75,"column":68},"action":"insert","lines":["g"]},{"start":{"row":75,"column":68},"end":{"row":75,"column":69},"action":"insert","lines":["e"]}],[{"start":{"row":75,"column":69},"end":{"row":75,"column":70},"action":"insert","lines":[" "],"id":305},{"start":{"row":75,"column":70},"end":{"row":75,"column":71},"action":"insert","lines":["h"]},{"start":{"row":75,"column":71},"end":{"row":75,"column":72},"action":"insert","lines":["a"]},{"start":{"row":75,"column":72},"end":{"row":75,"column":73},"action":"insert","lines":["s"]}],[{"start":{"row":75,"column":73},"end":{"row":75,"column":74},"action":"insert","lines":[" "],"id":306},{"start":{"row":75,"column":74},"end":{"row":75,"column":75},"action":"insert","lines":["r"]},{"start":{"row":75,"column":75},"end":{"row":75,"column":76},"action":"insert","lines":["e"]},{"start":{"row":75,"column":76},"end":{"row":75,"column":77},"action":"insert","lines":["d"]},{"start":{"row":75,"column":77},"end":{"row":75,"column":78},"action":"insert","lines":["i"]},{"start":{"row":75,"column":78},"end":{"row":75,"column":79},"action":"insert","lines":["r"]},{"start":{"row":75,"column":79},"end":{"row":75,"column":80},"action":"insert","lines":["e"]},{"start":{"row":75,"column":80},"end":{"row":75,"column":81},"action":"insert","lines":["c"]}],[{"start":{"row":75,"column":81},"end":{"row":75,"column":82},"action":"insert","lines":["t"],"id":307}],[{"start":{"row":75,"column":81},"end":{"row":75,"column":82},"action":"remove","lines":["t"],"id":308}],[{"start":{"row":75,"column":81},"end":{"row":75,"column":82},"action":"insert","lines":["t"],"id":309},{"start":{"row":75,"column":82},"end":{"row":75,"column":83},"action":"insert","lines":["e"]},{"start":{"row":75,"column":83},"end":{"row":75,"column":84},"action":"insert","lines":["d"]}],[{"start":{"row":85,"column":16},"end":{"row":85,"column":30},"action":"remove","lines":["Mac and cheese"],"id":310},{"start":{"row":85,"column":16},"end":{"row":85,"column":28},"action":"insert","lines":["Pumpkin rice"]}],[{"start":{"row":75,"column":87},"end":{"row":76,"column":74},"action":"remove","lines":["","        \"\"\"Delete recipe and check recipe is not present after redirect\"\"\""],"id":311}],[{"start":{"row":77,"column":8},"end":{"row":77,"column":60},"action":"remove","lines":["# use regular expression to find Object id of recipe"],"id":312},{"start":{"row":77,"column":8},"end":{"row":77,"column":66},"action":"insert","lines":["# Test regular expressions to locate Object id of a recipe"]}],[{"start":{"row":79,"column":27},"end":{"row":80,"column":0},"action":"insert","lines":["",""],"id":313},{"start":{"row":80,"column":0},"end":{"row":80,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":80,"column":8},"end":{"row":80,"column":66},"action":"insert","lines":["# Test regular expressions to locate Object id of a recipe"],"id":314}],[{"start":{"row":80,"column":10},"end":{"row":80,"column":66},"action":"remove","lines":["Test regular expressions to locate Object id of a recipe"],"id":315},{"start":{"row":80,"column":10},"end":{"row":80,"column":11},"action":"insert","lines":["D"]},{"start":{"row":80,"column":11},"end":{"row":80,"column":12},"action":"insert","lines":["e"]},{"start":{"row":80,"column":12},"end":{"row":80,"column":13},"action":"insert","lines":["l"]},{"start":{"row":80,"column":13},"end":{"row":80,"column":14},"action":"insert","lines":["e"]},{"start":{"row":80,"column":14},"end":{"row":80,"column":15},"action":"insert","lines":["t"]},{"start":{"row":80,"column":15},"end":{"row":80,"column":16},"action":"insert","lines":["e"]}],[{"start":{"row":80,"column":16},"end":{"row":80,"column":17},"action":"insert","lines":[" "],"id":316},{"start":{"row":80,"column":17},"end":{"row":80,"column":18},"action":"insert","lines":["r"]},{"start":{"row":80,"column":18},"end":{"row":80,"column":19},"action":"insert","lines":["e"]},{"start":{"row":80,"column":19},"end":{"row":80,"column":20},"action":"insert","lines":["c"]},{"start":{"row":80,"column":20},"end":{"row":80,"column":21},"action":"insert","lines":["i"]},{"start":{"row":80,"column":21},"end":{"row":80,"column":22},"action":"insert","lines":["p"]},{"start":{"row":80,"column":22},"end":{"row":80,"column":23},"action":"insert","lines":["e"]}],[{"start":{"row":80,"column":23},"end":{"row":80,"column":24},"action":"insert","lines":[" "],"id":317},{"start":{"row":80,"column":24},"end":{"row":80,"column":25},"action":"insert","lines":["u"]},{"start":{"row":80,"column":25},"end":{"row":80,"column":26},"action":"insert","lines":["s"]},{"start":{"row":80,"column":26},"end":{"row":80,"column":27},"action":"insert","lines":["i"]},{"start":{"row":80,"column":27},"end":{"row":80,"column":28},"action":"insert","lines":["n"]},{"start":{"row":80,"column":28},"end":{"row":80,"column":29},"action":"insert","lines":["g"]}],[{"start":{"row":80,"column":29},"end":{"row":80,"column":30},"action":"insert","lines":[" "],"id":318},{"start":{"row":80,"column":30},"end":{"row":80,"column":31},"action":"insert","lines":["t"]}],[{"start":{"row":80,"column":30},"end":{"row":80,"column":31},"action":"remove","lines":["t"],"id":319}],[{"start":{"row":80,"column":30},"end":{"row":80,"column":31},"action":"insert","lines":["t"],"id":320},{"start":{"row":80,"column":31},"end":{"row":80,"column":32},"action":"insert","lines":["h"]},{"start":{"row":80,"column":32},"end":{"row":80,"column":33},"action":"insert","lines":["e"]}],[{"start":{"row":80,"column":33},"end":{"row":80,"column":34},"action":"insert","lines":[" "],"id":321},{"start":{"row":80,"column":34},"end":{"row":80,"column":35},"action":"insert","lines":["r"]},{"start":{"row":80,"column":35},"end":{"row":80,"column":36},"action":"insert","lines":["e"]}],[{"start":{"row":80,"column":36},"end":{"row":80,"column":37},"action":"insert","lines":["c"],"id":322},{"start":{"row":80,"column":37},"end":{"row":80,"column":38},"action":"insert","lines":["i"]},{"start":{"row":80,"column":38},"end":{"row":80,"column":39},"action":"insert","lines":["p"]},{"start":{"row":80,"column":39},"end":{"row":80,"column":40},"action":"insert","lines":["e"]},{"start":{"row":80,"column":40},"end":{"row":80,"column":41},"action":"insert","lines":["_"]}],[{"start":{"row":80,"column":41},"end":{"row":80,"column":42},"action":"insert","lines":["i"],"id":323},{"start":{"row":80,"column":42},"end":{"row":80,"column":43},"action":"insert","lines":["d"]}],[{"start":{"row":78,"column":8},"end":{"row":78,"column":11},"action":"remove","lines":["ids"],"id":324},{"start":{"row":78,"column":8},"end":{"row":78,"column":9},"action":"insert","lines":["r"]},{"start":{"row":78,"column":9},"end":{"row":78,"column":10},"action":"insert","lines":["e"]},{"start":{"row":78,"column":10},"end":{"row":78,"column":11},"action":"insert","lines":["c"]},{"start":{"row":78,"column":11},"end":{"row":78,"column":12},"action":"insert","lines":["i"]},{"start":{"row":78,"column":12},"end":{"row":78,"column":13},"action":"insert","lines":["p"]},{"start":{"row":78,"column":13},"end":{"row":78,"column":14},"action":"insert","lines":["e"]},{"start":{"row":78,"column":14},"end":{"row":78,"column":15},"action":"insert","lines":["+"]}],[{"start":{"row":78,"column":14},"end":{"row":78,"column":15},"action":"remove","lines":["+"],"id":325}],[{"start":{"row":78,"column":14},"end":{"row":78,"column":15},"action":"insert","lines":["_"],"id":326},{"start":{"row":78,"column":15},"end":{"row":78,"column":16},"action":"insert","lines":["i"]},{"start":{"row":78,"column":16},"end":{"row":78,"column":17},"action":"insert","lines":["d"]}],[{"start":{"row":79,"column":19},"end":{"row":79,"column":22},"action":"remove","lines":["ids"],"id":327},{"start":{"row":79,"column":19},"end":{"row":79,"column":28},"action":"insert","lines":["recipe_id"]}],[{"start":{"row":82,"column":58},"end":{"row":82,"column":61},"action":"remove","lines":["ids"],"id":328},{"start":{"row":82,"column":58},"end":{"row":82,"column":67},"action":"insert","lines":["recipe_id"]}],[{"start":{"row":80,"column":43},"end":{"row":81,"column":57},"action":"remove","lines":["","        # togo that delete recipe page using extracted id"],"id":329}],[{"start":{"row":84,"column":42},"end":{"row":84,"column":43},"action":"remove","lines":[" "],"id":330},{"start":{"row":84,"column":41},"end":{"row":84,"column":42},"action":"remove","lines":[" "]}],[{"start":{"row":84,"column":41},"end":{"row":84,"column":42},"action":"remove","lines":[" "],"id":331},{"start":{"row":84,"column":41},"end":{"row":85,"column":0},"action":"insert","lines":["",""]},{"start":{"row":85,"column":0},"end":{"row":85,"column":8},"action":"insert","lines":["        "]},{"start":{"row":85,"column":8},"end":{"row":86,"column":0},"action":"insert","lines":["",""]},{"start":{"row":86,"column":0},"end":{"row":86,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":86,"column":4},"end":{"row":86,"column":8},"action":"remove","lines":["    "],"id":332}],[{"start":{"row":86,"column":4},"end":{"row":91,"column":32},"action":"insert","lines":["def test_recipes(self):","        \"\"\"Test recipe list page loading\"\"\"","        res = self.client.get('/recipe-listing')","        data = res.data.decode('utf-8')","        assert res.status == '200 OK'","        assert 'Recipes' in data"],"id":333}],[{"start":{"row":86,"column":13},"end":{"row":86,"column":20},"action":"remove","lines":["recipes"],"id":334},{"start":{"row":86,"column":13},"end":{"row":86,"column":14},"action":"insert","lines":["4"]},{"start":{"row":86,"column":14},"end":{"row":86,"column":15},"action":"insert","lines":["0"]},{"start":{"row":86,"column":15},"end":{"row":86,"column":16},"action":"insert","lines":["4"]},{"start":{"row":86,"column":16},"end":{"row":86,"column":17},"action":"insert","lines":["_"]},{"start":{"row":86,"column":17},"end":{"row":86,"column":18},"action":"insert","lines":["e"]},{"start":{"row":86,"column":18},"end":{"row":86,"column":19},"action":"insert","lines":["r"]}],[{"start":{"row":86,"column":19},"end":{"row":86,"column":20},"action":"insert","lines":["r"],"id":335},{"start":{"row":86,"column":20},"end":{"row":86,"column":21},"action":"insert","lines":["o"]},{"start":{"row":86,"column":21},"end":{"row":86,"column":22},"action":"insert","lines":["r"]}],[{"start":{"row":87,"column":43},"end":{"row":88,"column":0},"action":"insert","lines":["",""],"id":336},{"start":{"row":88,"column":0},"end":{"row":88,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":88,"column":8},"end":{"row":88,"column":43},"action":"insert","lines":["\"\"\"Test recipe list page loading\"\"\""],"id":337}],[{"start":{"row":88,"column":16},"end":{"row":88,"column":40},"action":"remove","lines":["recipe list page loading"],"id":338},{"start":{"row":88,"column":16},"end":{"row":88,"column":17},"action":"insert","lines":["4"]},{"start":{"row":88,"column":17},"end":{"row":88,"column":18},"action":"insert","lines":["0"]},{"start":{"row":88,"column":18},"end":{"row":88,"column":19},"action":"insert","lines":["4"]}],[{"start":{"row":88,"column":19},"end":{"row":88,"column":20},"action":"insert","lines":[" "],"id":339},{"start":{"row":88,"column":20},"end":{"row":88,"column":21},"action":"insert","lines":["e"]},{"start":{"row":88,"column":21},"end":{"row":88,"column":22},"action":"insert","lines":["r"]},{"start":{"row":88,"column":22},"end":{"row":88,"column":23},"action":"insert","lines":["r"]},{"start":{"row":88,"column":23},"end":{"row":88,"column":24},"action":"insert","lines":["o"]},{"start":{"row":88,"column":24},"end":{"row":88,"column":25},"action":"insert","lines":["r"]}],[{"start":{"row":88,"column":25},"end":{"row":88,"column":26},"action":"insert","lines":[" "],"id":340},{"start":{"row":88,"column":26},"end":{"row":88,"column":27},"action":"insert","lines":["p"]},{"start":{"row":88,"column":27},"end":{"row":88,"column":28},"action":"insert","lines":["a"]},{"start":{"row":88,"column":28},"end":{"row":88,"column":29},"action":"insert","lines":["g"]},{"start":{"row":88,"column":29},"end":{"row":88,"column":30},"action":"insert","lines":["e"]}],[{"start":{"row":89,"column":32},"end":{"row":89,"column":46},"action":"remove","lines":["recipe-listing"],"id":341},{"start":{"row":89,"column":32},"end":{"row":89,"column":41},"action":"insert","lines":["andle_404"]}],[{"start":{"row":89,"column":32},"end":{"row":89,"column":33},"action":"insert","lines":["h"],"id":342}],[{"start":{"row":91,"column":35},"end":{"row":91,"column":36},"action":"remove","lines":["K"],"id":343},{"start":{"row":91,"column":34},"end":{"row":91,"column":35},"action":"remove","lines":["O"]},{"start":{"row":91,"column":33},"end":{"row":91,"column":34},"action":"remove","lines":[" "]},{"start":{"row":91,"column":32},"end":{"row":91,"column":33},"action":"remove","lines":["0"]},{"start":{"row":91,"column":31},"end":{"row":91,"column":32},"action":"remove","lines":["0"]},{"start":{"row":91,"column":30},"end":{"row":91,"column":31},"action":"remove","lines":["2"]}],[{"start":{"row":91,"column":30},"end":{"row":91,"column":31},"action":"insert","lines":["4"],"id":344},{"start":{"row":91,"column":31},"end":{"row":91,"column":32},"action":"insert","lines":["0"]},{"start":{"row":91,"column":32},"end":{"row":91,"column":33},"action":"insert","lines":["4"]}],[{"start":{"row":92,"column":16},"end":{"row":92,"column":23},"action":"remove","lines":["Recipes"],"id":345},{"start":{"row":92,"column":16},"end":{"row":92,"column":17},"action":"insert","lines":["a"]}],[{"start":{"row":92,"column":16},"end":{"row":92,"column":17},"action":"remove","lines":["a"],"id":346}],[{"start":{"row":92,"column":16},"end":{"row":92,"column":17},"action":"insert","lines":["P"],"id":347},{"start":{"row":92,"column":17},"end":{"row":92,"column":18},"action":"insert","lines":["a"]},{"start":{"row":92,"column":18},"end":{"row":92,"column":19},"action":"insert","lines":["g"]},{"start":{"row":92,"column":19},"end":{"row":92,"column":20},"action":"insert","lines":["e"]}],[{"start":{"row":92,"column":20},"end":{"row":92,"column":21},"action":"insert","lines":[" "],"id":348},{"start":{"row":92,"column":21},"end":{"row":92,"column":22},"action":"insert","lines":["n"]},{"start":{"row":92,"column":22},"end":{"row":92,"column":23},"action":"insert","lines":["o"]},{"start":{"row":92,"column":23},"end":{"row":92,"column":24},"action":"insert","lines":["t"]}],[{"start":{"row":92,"column":24},"end":{"row":92,"column":25},"action":"insert","lines":[" "],"id":349},{"start":{"row":92,"column":25},"end":{"row":92,"column":26},"action":"insert","lines":["f"]},{"start":{"row":92,"column":26},"end":{"row":92,"column":27},"action":"insert","lines":["o"]},{"start":{"row":92,"column":27},"end":{"row":92,"column":28},"action":"insert","lines":["u"]},{"start":{"row":92,"column":28},"end":{"row":92,"column":29},"action":"insert","lines":["n"]},{"start":{"row":92,"column":29},"end":{"row":92,"column":30},"action":"insert","lines":["d"]}],[{"start":{"row":86,"column":29},"end":{"row":87,"column":43},"action":"remove","lines":["","        \"\"\"Test recipe list page loading\"\"\""],"id":350}],[{"start":{"row":55,"column":37},"end":{"row":56,"column":0},"action":"insert","lines":["",""],"id":351},{"start":{"row":56,"column":0},"end":{"row":56,"column":8},"action":"insert","lines":["        "]},{"start":{"row":56,"column":8},"end":{"row":57,"column":0},"action":"insert","lines":["",""]},{"start":{"row":57,"column":0},"end":{"row":57,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":57,"column":4},"end":{"row":68,"column":39},"action":"insert","lines":["def test_recipe_page(self):","        \"\"\"Find Recipe and go to it's recipe page\"\"\"","        res = self.client.get('/recipes')","        # use regular expression to find Object id of recipe","        ids = re.findall(r'href=\"/recipe/(\\w+)\"', res.data.decode(\"utf8\"))","        # check we have something","        assert len(ids) > 0","        # to go that recipe page using extracted id","        res = self.client.get('/recipe/{}'.format(ids[0]))","        data = res.data.decode('utf-8')","        assert res.status == '200 OK'","        assert 'Mac and cheese' in data"],"id":352}],[{"start":{"row":57,"column":13},"end":{"row":57,"column":19},"action":"remove","lines":["recipe"],"id":353},{"start":{"row":57,"column":13},"end":{"row":57,"column":14},"action":"insert","lines":["s"]},{"start":{"row":57,"column":14},"end":{"row":57,"column":15},"action":"insert","lines":["e"]},{"start":{"row":57,"column":15},"end":{"row":57,"column":16},"action":"insert","lines":["a"]},{"start":{"row":57,"column":16},"end":{"row":57,"column":17},"action":"insert","lines":["r"]},{"start":{"row":57,"column":17},"end":{"row":57,"column":18},"action":"insert","lines":["c"]},{"start":{"row":57,"column":18},"end":{"row":57,"column":19},"action":"insert","lines":["h"]}],[{"start":{"row":58,"column":11},"end":{"row":58,"column":49},"action":"remove","lines":["Find Recipe and go to it's recipe page"],"id":354},{"start":{"row":58,"column":11},"end":{"row":58,"column":74},"action":"insert","lines":["est finding a recipe and redirect to that recipes specific page"]}],[{"start":{"row":58,"column":11},"end":{"row":58,"column":12},"action":"insert","lines":["T"],"id":355}],[{"start":{"row":58,"column":49},"end":{"row":58,"column":70},"action":"remove","lines":["that recipes specific"],"id":356},{"start":{"row":58,"column":49},"end":{"row":58,"column":50},"action":"insert","lines":["s"]},{"start":{"row":58,"column":50},"end":{"row":58,"column":51},"action":"insert","lines":["e"]},{"start":{"row":58,"column":51},"end":{"row":58,"column":52},"action":"insert","lines":["a"]},{"start":{"row":58,"column":52},"end":{"row":58,"column":53},"action":"insert","lines":["r"]},{"start":{"row":58,"column":53},"end":{"row":58,"column":54},"action":"insert","lines":["c"]},{"start":{"row":58,"column":54},"end":{"row":58,"column":55},"action":"insert","lines":["h"]}],[{"start":{"row":58,"column":55},"end":{"row":58,"column":56},"action":"insert","lines":[" "],"id":357},{"start":{"row":58,"column":56},"end":{"row":58,"column":57},"action":"insert","lines":["p"]},{"start":{"row":58,"column":57},"end":{"row":58,"column":58},"action":"insert","lines":["a"]}],[{"start":{"row":58,"column":57},"end":{"row":58,"column":58},"action":"remove","lines":["a"],"id":358},{"start":{"row":58,"column":56},"end":{"row":58,"column":57},"action":"remove","lines":["p"]},{"start":{"row":58,"column":55},"end":{"row":58,"column":56},"action":"remove","lines":[" "]}],[{"start":{"row":58,"column":16},"end":{"row":58,"column":23},"action":"remove","lines":["finding"],"id":359},{"start":{"row":58,"column":15},"end":{"row":58,"column":16},"action":"remove","lines":[" "]}],[{"start":{"row":58,"column":15},"end":{"row":58,"column":16},"action":"insert","lines":[" "],"id":360},{"start":{"row":58,"column":16},"end":{"row":58,"column":17},"action":"insert","lines":["s"]},{"start":{"row":58,"column":17},"end":{"row":58,"column":18},"action":"insert","lines":["e"]},{"start":{"row":58,"column":18},"end":{"row":58,"column":19},"action":"insert","lines":["a"]},{"start":{"row":58,"column":19},"end":{"row":58,"column":20},"action":"insert","lines":["r"]},{"start":{"row":58,"column":20},"end":{"row":58,"column":21},"action":"insert","lines":["c"]},{"start":{"row":58,"column":21},"end":{"row":58,"column":22},"action":"insert","lines":["h"]},{"start":{"row":58,"column":22},"end":{"row":58,"column":23},"action":"insert","lines":["i"]},{"start":{"row":58,"column":23},"end":{"row":58,"column":24},"action":"insert","lines":["n"]},{"start":{"row":58,"column":24},"end":{"row":58,"column":25},"action":"insert","lines":["g"]}],[{"start":{"row":58,"column":25},"end":{"row":58,"column":26},"action":"insert","lines":[" "],"id":361},{"start":{"row":58,"column":26},"end":{"row":58,"column":27},"action":"insert","lines":["f"]},{"start":{"row":58,"column":27},"end":{"row":58,"column":28},"action":"insert","lines":["o"]},{"start":{"row":58,"column":28},"end":{"row":58,"column":29},"action":"insert","lines":["r"]}],[{"start":{"row":58,"column":29},"end":{"row":58,"column":30},"action":"insert","lines":[" "],"id":362}],[{"start":{"row":58,"column":29},"end":{"row":58,"column":30},"action":"remove","lines":[" "],"id":363}],[{"start":{"row":59,"column":32},"end":{"row":59,"column":39},"action":"remove","lines":["recipes"],"id":364},{"start":{"row":59,"column":32},"end":{"row":59,"column":33},"action":"insert","lines":["s"]},{"start":{"row":59,"column":33},"end":{"row":59,"column":34},"action":"insert","lines":["e"]},{"start":{"row":59,"column":34},"end":{"row":59,"column":35},"action":"insert","lines":["a"]},{"start":{"row":59,"column":35},"end":{"row":59,"column":36},"action":"insert","lines":["r"]},{"start":{"row":59,"column":36},"end":{"row":59,"column":37},"action":"insert","lines":["c"]},{"start":{"row":59,"column":37},"end":{"row":59,"column":38},"action":"insert","lines":["h"]}],[{"start":{"row":60,"column":8},"end":{"row":60,"column":60},"action":"remove","lines":["# use regular expression to find Object id of recipe"],"id":365},{"start":{"row":60,"column":8},"end":{"row":60,"column":66},"action":"insert","lines":["# Test regular expressions to locate Object id of a recipe"]}],[{"start":{"row":61,"column":8},"end":{"row":61,"column":11},"action":"remove","lines":["ids"],"id":366},{"start":{"row":61,"column":8},"end":{"row":61,"column":17},"action":"insert","lines":["recipe_id"]}],[{"start":{"row":63,"column":19},"end":{"row":63,"column":22},"action":"remove","lines":["ids"],"id":367},{"start":{"row":63,"column":19},"end":{"row":63,"column":28},"action":"insert","lines":["recipe_id"]}],[{"start":{"row":65,"column":50},"end":{"row":65,"column":53},"action":"remove","lines":["ids"],"id":368},{"start":{"row":65,"column":50},"end":{"row":65,"column":59},"action":"insert","lines":["recipe_id"]}],[{"start":{"row":59,"column":40},"end":{"row":63,"column":33},"action":"remove","lines":["","        # Test regular expressions to locate Object id of a recipe","        recipe_id = re.findall(r'href=\"/recipe/(\\w+)\"', res.data.decode(\"utf8\"))","        # check we have something","        assert len(recipe_id) > 0"],"id":369}],[{"start":{"row":61,"column":8},"end":{"row":61,"column":64},"action":"remove","lines":["res = self.client.get('/recipe/{}'.format(recipe_id[0]))"],"id":370},{"start":{"row":61,"column":8},"end":{"row":68,"column":10},"action":"insert","lines":["res = self.client.post('/create_recipe', follow_redirects=True, data={","            'recipe_name': 'Pumpkin rice',","            'recipe_description': 'From brownies and pancakes to veggie-packed curries, stir-fries and salads, these vegan recipes are vibrant and delicious.',","            'recipe_ingredients': '400g pumpkin, or butternut squash',","            'recipe_instructions': 'Add all of the ingredients',","            'recipe_keywords': 'vegan, pumpkin, rice, butternut squash',","            'recipe_image_url': 'image url goes here'","        })"]}],[{"start":{"row":71,"column":8},"end":{"row":71,"column":40},"action":"remove","lines":["assert 'Mac and cheese' in data "],"id":371},{"start":{"row":71,"column":8},"end":{"row":75,"column":29},"action":"insert","lines":["assert 'vegan' in data","        assert 'Pumpkin' in data","        assert 'delicious' in data","        assert 'butternut' in data","        assert 'here' in data"]}],[{"start":{"row":61,"column":29},"end":{"row":61,"column":30},"action":"remove","lines":["t"],"id":372},{"start":{"row":61,"column":28},"end":{"row":61,"column":29},"action":"remove","lines":["s"]},{"start":{"row":61,"column":27},"end":{"row":61,"column":28},"action":"remove","lines":["o"]},{"start":{"row":61,"column":26},"end":{"row":61,"column":27},"action":"remove","lines":["p"]}],[{"start":{"row":61,"column":26},"end":{"row":61,"column":27},"action":"insert","lines":["g"],"id":373},{"start":{"row":61,"column":27},"end":{"row":61,"column":28},"action":"insert","lines":["e"]},{"start":{"row":61,"column":28},"end":{"row":61,"column":29},"action":"insert","lines":["t"]}],[{"start":{"row":61,"column":32},"end":{"row":61,"column":45},"action":"remove","lines":["create_recipe"],"id":374},{"start":{"row":61,"column":32},"end":{"row":61,"column":33},"action":"insert","lines":["s"]},{"start":{"row":61,"column":33},"end":{"row":61,"column":34},"action":"insert","lines":["e"]},{"start":{"row":61,"column":34},"end":{"row":61,"column":35},"action":"insert","lines":["a"]},{"start":{"row":61,"column":35},"end":{"row":61,"column":36},"action":"insert","lines":["r"]},{"start":{"row":61,"column":36},"end":{"row":61,"column":37},"action":"insert","lines":["c"]},{"start":{"row":61,"column":37},"end":{"row":61,"column":38},"action":"insert","lines":["h"]}],[{"start":{"row":64,"column":0},"end":{"row":64,"column":70},"action":"remove","lines":["            'recipe_ingredients': '400g pumpkin, or butternut squash',"],"id":375},{"start":{"row":63,"column":159},"end":{"row":64,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":65,"column":72},"end":{"row":66,"column":53},"action":"remove","lines":["","            'recipe_image_url': 'image url goes here'"],"id":376},{"start":{"row":65,"column":71},"end":{"row":65,"column":72},"action":"remove","lines":[","]}],[{"start":{"row":72,"column":34},"end":{"row":73,"column":30},"action":"remove","lines":["","        assert 'here' in data "],"id":377}],[{"start":{"row":58,"column":69},"end":{"row":60,"column":51},"action":"remove","lines":["","        res = self.client.get('/search')","        # to go that recipe page using extracted id"],"id":378}]]},"ace":{"folds":[],"scrolltop":103,"scrollleft":18,"selection":{"start":{"row":11,"column":20},"end":{"row":11,"column":20},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":74,"state":"start","mode":"ace/mode/python"}},"timestamp":1575714919878,"hash":"22a61b6915e4eece9d9bb004c24a283e9667436f"}