from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')\

@app.route('/hello')
def index2():
    make_map()
    return render_template('test.html')

if __name__ == "__main__":
    def tri_bulle1(tab):
        n = len(tab)
        # Traverser tous les éléments du tableau
        for i in range(n):
            for j in range(1, n - i - 1):
                # échanger si l'élément trouvé est plus grand que le suivant
                if tab[j] < tab[j + 1]:
                    tab[j], tab[j + 1] = tab[j + 1], tab[j]


    from pyroutelib3 import Router
    import folium
    import os

    def make_map():
        """
            créer la carte (fichier HTML + openstreetmap + javascript)
            Attention réponse assez longue : parfois plusieurs minutes !
            https://github.com/MKuranowski/pyroutelib3/issues/3
            """
        c = folium.Map(location=[36.841114, 10.246388], zoom_start=15)
        coor_depart = [36.841114, 10.246388]  # lycée Branly
        # 36.836848, 10.173702
        list1 = [[36.841114, 10.246388]]
        # for i in range (0,4): len list elli jeybin menha mel base # apres list . append list(base)[i]
        # 36.836848, 10.173702
        list1.append([36.844115, 10.182878])
        # list1.append([36.802520, 10.127349])
        # 36.813557535277425, 10.133855432155167
        list1.append([36.840840, 10.174903])
        list1.append([36.813557535277425, 10.133855432155167])
        list1.append([36.836848, 10.173702])
        # list1.append([36.864732, 10.155239])
        print(list1)
        coor_intermidiaire = [36.802520, 10.127349]
        coor_arrivee = [36.813557535277425, 10.133855432155167]  # théatre Monsigny
        # coor_arrivee= [50.72712, 1.60874] # bug
        # marquer sur la carte les points de départ et d'arrivée
        for i in range(len(list1)):
            folium.Marker(list1[i], popup="Départ").add_to(c)
        print("debut routage, veuillez patientez svp ...")
        # router = Router("car","map.osm")
        router = Router("car")
        depart = list()
        # tri_bulle(list1)
        for i in range(len(list1)):
            a = router.findNode(list1[i][0], list1[i][1])
            depart.append(a)
            print(depart)
        # tri_bulle(list1)
        tri_bulle1(depart)
        # status = list()
        route = list()
        for i in range(1, len(list1)):
            route.append(router.doRoute(depart[i - 1], depart[i]))
        # status1, route1 = router.doRoute(depart[1], depart[2])
        # else:
        #   status, route = router.doRoute(depart[0], depart[2])
        #  status1, route1 = router.doRoute(depart[2], depart[1])
        # if status == 'success':
        #    print("route trouvée")
        routeLatLons = list()
        for i in range(len(list1) - 1):
            print(route[1][1])
            # routeLatLons += list(map(router.nodeLatLon, route[i][1]))
            routeLatLons.append(list(map(router.nodeLatLon, route[i][1])))
            # routeLatLons1 = list(map(router.nodeLatLon, route1))
        # else:
        #    print("route pas trouvée !")
        print(list1)
        for i in range(len(list1) - 1):
            for coord in routeLatLons[i]:
                coord = list(coord)
                folium.CircleMarker(coord, radius=3, fill=True, color='red').add_to(c)
        for i in range(len(list1) - 1):
            folium.PolyLine(routeLatLons[i], color="green", weight=2.5, opacity=1).add_to(c)
        # for coord in routeLatLons1:
        #    coord=list(coord)
        #    folium.CircleMarker(coord,radius = 3,fill=True, color='red' ).add_to(c)

        # folium.PolyLine(routeLatLons, color="green", weight=2.5, opacity=1).add_to(c)
        # folium.PolyLine(routeLatLons1, color="green", weight=2.5, opacity=1).add_to(c)
        print("Le fichier HTML/CARTE est disponible")
        fichier_carte = 'test.html'
        c.save('templates/test.html')
        print(c.get_root)
        # c.key

        # ouvrir le fichier dans le navigateur
        rep_cour = os.getcwd()
        fichier = 'firefox file://' + rep_cour + '/' + fichier_carte
        os.popen(fichier);
    app.run()