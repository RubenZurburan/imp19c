def print_industrial_goods_scripted_guis(goods_name):
	print("add_{goods_name}_button = {{\n    scope = governorship\n    saved_scopes = {{ player }}\n    confirm_title = \"{goods_name}_industry_confirm_title\"\n    confirm_text = \"{goods_name}_industry_confirm_desc\"\n\n    is_valid = {{\n        #Tech Triggers\n    }}\n    effect = {{\n        save_scope_as = governorship_name\n        if = {{\n            limit = {{\n                INDUSTRY_governorship_total_industry_slots > INDUSTRY_governorship_used_industry_slots\n                has_variable = INDUSTRY_factories_assigned_{goods_name}\n            }}\n            scope:player = {{ pay_price = add_industry_price }}\n            change_variable = {{\n                name = INDUSTRY_factories_assigned_{goods_name}\n                add = 1\n            }}\n            custom_tooltip = {goods_name}_add_button_tt\n        }}\n    }}\n}}\nremove_{goods_name}_button = {{\n    scope = governorship\n    confirm_title = \"{goods_name}_industry_remove_confirm_title\"\n    confirm_text = \"{goods_name}_industry_remove_confirm_desc\"\n\n    effect = {{\n        if = {{\n            limit = {{\n                INDUSTRY_governorship_total_industry_slots > INDUSTRY_governorship_used_industry_slots\n            }}\n            custom_tooltip = two_newlines_tooltip\n        }}\n        save_scope_as = governorship_name\n        show_as_tooltip = {{ scope:player = {{ pay_price = remove_industry_price }} }}\n        if = {{\n            limit = {{\n                var:INDUSTRY_factories_assigned_{goods_name} > 0\n                scope:player = {{ can_pay_price = remove_industry_price }}\n            }}\n            hidden_effect = {{ scope:player = {{ pay_price = remove_industry_price }} }}\n            change_variable = {{\n                name = INDUSTRY_factories_assigned_{goods_name}\n                subtract = 1\n            }}\n        }}\n        custom_tooltip = {goods_name}_remove_button_tt\n    }}\n}}".format(goods_name=goods_name))

def industrial_goods_localization(goods_name):
	caps_name = goods_name.upper()
	lowercase_name = goods_name.lower()
	initial_cap_name = goods_name.replace("_", " ").title()
	print("PROVWINDOW_GOV_{caps_name}_PRODUCED_TT:0 \"#T {initial_cap_name} Industry#!\\n[GetScriptedGui('add_{lowercase_name}_button').BuildTooltip( GuiScope.SetRoot( ProvinceWindow.GetState.GetGovernorship.MakeScope ).AddScope('player', Player.MakeScope ).End )][GetScriptedGui('remove_{lowercase_name}_button').BuildTooltip( GuiScope.SetRoot( ProvinceWindow.GetState.GetGovernorship.MakeScope ).AddScope('player', Player.MakeScope ).End)]\\n\\n#TF [ProvinceWindow.GetState.GetGovernorship.GetNameWithNoTooltip] currently has [GuiScope.SetRoot(ProvinceWindow.GetState.GetGovernorship.MakeScope).ScriptValue('INDUSTRY_{lowercase_name}_factories')|0] {initial_cap_name} industries.\\nLeft click to increase {initial_cap_name} industries.\\nRight click to decrease {initial_cap_name} industries.#!\"".format(caps_name=caps_name,lowercase_name=lowercase_name,initial_cap_name=initial_cap_name))
	print("{lowercase_name}_add_button_tt:0 \"[governorship_name.GetName] gains #Q 1#! {initial_cap_name} industry\"".format(caps_name=caps_name,lowercase_name=lowercase_name,initial_cap_name=initial_cap_name))
	print("{lowercase_name}_remove_button_tt:0 \"Remove #X 1#! {initial_cap_name} industry from [governorship_name.GetName].\"".format(caps_name=caps_name,lowercase_name=lowercase_name,initial_cap_name=initial_cap_name))
	print("{goods_name}_industry_confirm_title:0 \" Increase {initial_cap_name} Industries \"".format(goods_name=goods_name,initial_cap_name=initial_cap_name))
	print("{goods_name}_industry_confirm_desc:0 \" Are you sure you want to increase {initial_cap_name} industries?\"".format(goods_name=goods_name,initial_cap_name=initial_cap_name))
	print("{goods_name}_industry_remove_confirm_title:0 \" Decrease {initial_cap_name} Industries\"".format(goods_name=goods_name,initial_cap_name=initial_cap_name))
	print("{goods_name}_industry_remove_confirm_desc:0 \" Are you sure you want to decrease {initial_cap_name} industries?\"\n".format(goods_name=goods_name,initial_cap_name=initial_cap_name))

all_goods = ["clothing","luxury_clothing","furniture","luxury_furniture","alcohol","glass","chemicals","rare_alloys","construction_materials","early_munitions","late_munitions","naval_supplies","steel_ships","wooden_ships","steel","bronze","machine_parts","early_artillery","late_artillery","electronics","pharmaceuticals","motors","processed_foods","petrochemicals"]
		
for good in all_goods:
	industrial_goods_localization(good)
#	print_industrial_goods_scripted_guis(good)