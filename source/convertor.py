import json
import csv
import sys

#open the input json file
with open(sys.argv[1],encoding='utf8') as f:
	data = json.load(f)

#create the output.csv file
with open('output.csv', 'w', newline='',encoding='utf8') as csvfile:
	headers = ["id","lang","foil","nonfoil","promo","set","rarity","mana_cost","story_spotlight","uri","oracle_text","variation","full_art","legalities","set_type","digital","keywords","object","scryfall_set_uri","border_color","highres_image","oversized","textless","games","set_name","illustration_id","produced_mana","frame","colors","scryfall_uri","tcgplayer_id","prices","oracle_id","color_identity","reprint","name","set_id","artist_ids","reserved","mtgo_id","prints_search_uri","rulings_uri","related_uris","released_at","type_line","arena_id","image_status","set_uri","purchase_uris","card_back_id","layout","artist","multiverse_ids","cmc","booster","collector_number","image_uris","finishes","set_search_uri","image","power","cardmarket_id","mtgo_foil_id","edhrec_rank","toughness","penny_rank","flavor_text","promo_types","all_parts","security_stamp","artist_id","card_faces","preview","watermark","frame_effects","loyalty","defense","tcgplayer_etched_id","flavor_name","attraction_lights","color_indicator","variation_of","hand_modifier","life_modifier","content_warning","printed_text","printed_type_line","printed_name"]
	thewriter = csv.DictWriter(csvfile,fieldnames=headers)

	#only writes the columns defined here.
	thewriter.writeheader()
	for card in data:
		if 'lang' in card:
			if card['lang'] == 'cfgvnjfdgvjmxvb':
				continue
			else:
				#Only save the 'normal' sized image link to the CSV
				if 'image_uris' in card:
					card["image"] = card['image_uris']['normal']
				#only use front facing card face if there are multiple faces
				if 'card_faces' in card:
					if 'image_uris' in card['card_faces'][0]:
						card["image"] = card['card_faces'][0]['image_uris']['normal']
					name = card['name']
					if 'type_line' in card:
						type = card['type_line']
					card.update(card['card_faces'][0])
					card['name'] = name
					if type is not None:
						card['type_line'] = type
			thewriter.writerow(card)
