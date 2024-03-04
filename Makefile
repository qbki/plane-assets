to-glb:
	@python3 ./scripts/used-blend.py \
		| xargs --verbose -i \
			blender \
				--background \
				{} \
				--python ./scripts/blend2glb.py
.PHONY: build

remove-unused:
	@python3 ./scripts/unused-glb.py | xargs rm
.PHONY: remove-unused
