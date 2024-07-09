all:
	make master
	
	make mapper1
	make mapper2
	make mapper3
	make mapper4
	make mapper5

	make reducer1
	make reducer2

master:
	python3 master.py

mapper0:
	python3 mapper.py --port 50050

mapper1:
	python3 mapper.py --port 50051

mapper2:
	python3 mapper.py --port 50052

mapper3:
	python3 mapper.py --port 50053

mapper4:
	python3 mapper.py --port 50054

reducer0:
	python3 reducer.py --port 50060

reducer1:
	python3 reducer.py --port 50061

reducer2:
	python3 reducer.py --port 50062

clean:
	rm -f Mappers/*/*.txt
	rm -f Reducers/*.txt