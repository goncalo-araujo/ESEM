#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px


# In[2]:


ac = pd.read_csv("ac_types.csv")
dhw = pd.read_csv("dhw_types.csv")


# In[3]:


st.write("""
# Energy system simulation model for your home

This web application calculates a building, home, or room final and primary energies according to the set inputs.
""")
st.write("---")


# In[37]:


st.header('Please specify the equipments you wish to account for in the model:')

options = st.multiselect("Electric Equipments:", ["TV", 
                                                  "Light Sources", 
                                                  "Computer", 
                                                  "Laptop", 
                                                  "Washing Machine", 
                                                  "Dish Washer", 
                                                  "Fridge", 
                                                  "Microwave", 
                                                  "Oven", 
                                                  "Cooktop",
                                                  "DHW equipments",
                                                  "Climatization equipments"], default=["TV", 
                                                                                        "Light Sources",
                                                                                        "Laptop",
                                                                                        "Climatization equipments"])

st.write("---")
source_options = ["Natural Gas", "Electricity", "Biomass", "Renewables"]


# In[69]:


if "Light Sources" in options:
    st.header("Light Sources inputs:")
    type_lights = st.multiselect("Types of light sources:", ["Living Room", 
                                                             "Corridor", 
                                                             "Kitchen", 
                                                             "Bedroom", 
                                                             "Office", 
                                                             "Bathroom"], default=["Office", "Kitchen"])
    lights_source = st.selectbox("Specify the energy source for the lights:", source_options, index=1)
    lights=np.array([])
    if "Living Room" in type_lights:
        st.subheader("Living room lights:")
        n_living_lights = st.number_input("Number of light sources in the living room:", min_value=1, value=4)
        p_living_lights = st.number_input("Mean living room light source Wattage (W):", min_value=1, value= 5)
        t_living_lights = st.slider("Number of hours of light in  the living room per week:", min_value=0, max_value=168, value=14)
        lights = np.append(lights, ["Lightbulbs", n_living_lights, p_living_lights, t_living_lights, lights_source])
    if "Corridor" in type_lights:
        st.subheader("Corridor lights")
        n_corr_lights = st.number_input("Number of light sources in the corridor:", min_value=1, value=4)
        p_corr_lights = st.number_input("Mean corridor light source Wattage (W):", min_value=1, value= 6)
        t_corr_lights = st.slider("Number of hours of light in  the corridor per week:", min_value=0, max_value=168, value=7)
        lights = np.append(lights, ["Lightbulbs", n_corr_lights, p_corr_lights, t_corr_lights, lights_source])
    if "Kitchen" in type_lights:
        st.subheader("Kitchen lights")
        n_kitch_lights = st.number_input("Number of light sources in the kitchen:", min_value=1, value=2)
        p_kitch_lights = st.number_input("Mean kitchen light source Wattage (W):", min_value=1, value= 18)
        t_kitch_lights = st.slider("Number of hours of light in  the kitchen per week:", min_value=0, max_value=168, value=14)
        lights = np.append(lights, ["Lightbulbs", n_kitch_lights, p_kitch_lights, t_kitch_lights, lights_source])
    if "Bedroom" in type_lights:
        st.subheader("Bedroom lights")
        n_bed_lights = st.number_input("Number of light sources in the bedrooms:", min_value=1, value=2)
        p_bed_lights = st.number_input("Mean bedroom light source Wattage (W):", min_value=1, value= 10)
        t_bed_lights = st.slider("Number of hours of light in  the bedrooms per week:", min_value=0, max_value=168, value= 7)
        lights = np.append(lights, ["Lightbulbs", n_bed_lights, p_bed_lights, t_bed_lights, lights_source])
    if "Office" in type_lights:
        st.subheader("Office lights")
        n_office_lights = st.number_input("Number of light sources in the offices:", min_value=1, value=2)
        p_office_lights = st.number_input("Mean office light source Wattage (W):", min_value=1, value= 9)
        t_office_lights = st.slider("Number of hours of light in  the offices per week:", min_value=0, max_value=168, value= 14)
        lights = np.append(lights, ["Lightbulbs", n_office_lights, p_office_lights, t_office_lights, lights_source])
    if "Bathroom" in type_lights:
        st.subheader("Bathroom lights")
        n_bath_lights = st.number_input("Number of light sources in the bathroom:", min_value=1, value=2)
        p_bath_lights = st.number_input("Mean office light source Wattage (W):", min_value=1, value= 8)
        t_bath_lights = st.slider("Number of hours of light in  the bathroom per week:", min_value=0, max_value=168, value= 14)
        lights = np.append(lights, ["Lightbulbs", n_bath_lights, p_bath_lights, t_bath_lights, lights_source])
        
    st.write("---")

        


# In[70]:


lights = lights.reshape((int(len(lights)/5), 5))


# In[71]:


tv = np.array([])
if "TV" in options:
    st.header("TV inputs:")
    n_tv = st.number_input("Number of TVs': ", min_value=1, value=2)
    p_tv = st.number_input("Mean TV Wattage (W):", min_value=50, value=100)
    t_tv = st.slider("Number of hours of TV use per week:", min_value=1, max_value=168, value=14)
    st.write("---")
    tv = np.append(tv, ["TV", n_tv, p_tv, t_tv, source_options[1]])
    tv = tv.reshape(1, 5)


# In[72]:


computer = np.array([])
if "Computer" in options:
    st.header("Computer inputs:")
    n_computer = st.number_input("Number of computers: ", min_value=1, value=1)
    p_computer = st.number_input("Mean computer Wattage (W):", min_value=50, value=200)
    t_computer = st.slider("Number of hours of computer use per week:", min_value=1, max_value=168, value=30)
    st.write("---")
    computer = np.append(computer, ["Computer", n_computer, p_computer, t_computer, source_options[1]])
    computer = computer.reshape(1, 5)


# In[73]:


laptop=np.array([])
if "Laptop" in options:
    st.header("Laptop inputs:")
    n_laptop = st.number_input("Number of laptops: ", min_value=1, value=2)
    p_laptop = st.number_input("Mean laptop Wattage (W):", min_value=50, value=50)
    t_laptop = st.slider("Number of hours of laptop use per week:", min_value=1, max_value=168, value=6)
    st.write("---")
    laptop = np.append(laptop, ["Laptop", n_laptop, p_laptop, t_laptop, source_options[1]])
    laptop = laptop.reshape(1, 5)


# In[74]:


wash = np.array([])
if "Washing Machine" in options:
    st.header("Washing Machine inputs:")
    n_wash = st.number_input("Number of washing machines: ", min_value=1, value=1)
    p_wash = st.number_input("Mean washing machine Wattage (W):", min_value=50, value=500)
    t_wash = st.slider("Number of hours of washing machine use per week:", min_value=1, max_value=168, value=6)
    st.write("---")
    wash = np.append(wash, ["Washing machine", n_wash, p_wash, t_wash, source_options[1]])
    wash = wash.reshape(1, 5)


# In[75]:


dish=np.array([])
if "Dish Washer" in options:
    st.header("Dish Washer inputs:")
    n_dish = st.number_input("Number of dish washers: ", min_value=1, value=1)
    p_dish = st.number_input("Mean dish washer Wattage (W):", min_value=50, value=1400)
    t_dish = st.slider("Number of hours of dish washer use per week:", min_value=1, max_value=168, value=9)
    st.write("---")
    dish = np.append(dish, ["Dish washer", n_dish, p_dish, t_dish, source_options[1]])
    dish = dish.reshape(n_dish, 5)


# In[76]:


fridge=np.array([])
if "Fridge" in options:
    st.header("Fridge inputs:")
    n_fridge = st.number_input("Number of fridges: ", min_value=1, value=1)
    p_fridge = st.number_input("Mean fridge Wattage (W):", min_value=50, value=400)
    t_fridge = 168
    st.write("---")
    fridge = np.append(fridge, ["Fridge", n_fridge, p_fridge, t_fridge, source_options[1]])
    fridge = fridge.reshape(1, 5)


# In[77]:


microwave = np.array([])
if "Microwave" in options:
    st.header("Microwave inputs:")
    n_micro = st.number_input("Number of microwaves: ", min_value=1, value=1)
    p_micro = st.number_input("Mean microwave Wattage (W):", min_value=50, value=750)
    t_micro = st.slider("Number of hours of microwaver use per week:", min_value=1, max_value=168, value=1)
    st.write("---")
    microwave = np.append(microwave, ["Microwave", n_micro, p_micro, t_micro, source_options[1]])
    microwave = microwave.reshape(n_micro, 5)


# In[78]:


oven=np.array([])
if "Oven" in options:
    st.header("Oven inputs:")
    n_oven = st.number_input("Number of ovens: ", min_value=1, value=1)
    p_oven = st.number_input("Mean oven Wattage (W):", min_value=50, value=3000)
    t_oven = st.slider("Number of hours of oven use per week:", min_value=1, max_value=168, value=3)
    st.write("---")
    oven = np.append(oven, ["Oven", n_oven, p_oven, t_oven, source_options[1]])
    oven = oven.reshape(1, 5)


# In[79]:


cooktop=np.array([])
if "Cooktop" in options:
    st.header("Cooktop inputs:")
    n_cook = st.number_input("Number of Cooktops: ", min_value=1, value=1)
    p_cook = st.number_input("Mean Cooktop Wattage (W):", min_value=50, value=1500)
    t_cook = st.slider("Number of hours of Cooktop use per week:", min_value=1, max_value=168, value=6)
    st.write("---")
    cooktop = np.append(cooktop, ["Cooktop", n_cook, p_cook, t_cook, source_options[1]])
    cooktop = cooktop.reshape(1, 5)


# In[80]:


dhw.index = dhw["0"]


# In[81]:


dhw_t=np.array([])
if "DHW equipments" in options:
    st.header("DHW equipments inputs:")
    type_dhw = st.selectbox("Type of DHW equipment", dhw["0"], index=0)
    dhw_source = st.selectbox("Specify the energy source for the DHW:", source_options, index=0)
    n_dhw = st.number_input("Number of DHW equipments: ", min_value=1, value=1)
    p_dhw = st.number_input("DHW equipment Wattage (W):", min_value=50, value=dhw["1"].loc[type_dhw])
    t_dhw = st.slider("Number of hours of hot water use per week:", min_value=1, max_value=168, value=4)
    st.write("---")
    dhw_t = np.append(dhw_t, ["DHW", n_dhw, p_dhw, t_dhw, dhw_source])
    dhw_t = dhw_t.reshape(1, 5)


# In[82]:


ac.index = ac["0"]


# In[83]:


ac_equips=np.array([])
if "Climatization equipments" in options:
    st.header("Climatization equipments inputs:")
    type_ac = st.multiselect("Type of Climatization equipment", ac["0"].values, default=["Split"])
    
    
    if "Portable AC" in type_ac:
        pac_source = st.selectbox("Specify the energy source for the AC unit:", source_options, index=1)
        n_porac = st.number_input("Number of Portable AC equipments: ", min_value=1, value=1)
        p_porac = st.number_input("Portable AC equipment Wattage (W):", min_value=50, value=ac["1"].iloc[0])
        t_porac = st.slider("Number of hours of hot water use per week:", min_value=1, max_value=168, value=7)
        ac_equips = np.append(ac_equips, ["Portable AC", n_porac, p_porac, t_porac, pac_source])
    
    if "Heater" in type_ac:
        hac_source = st.selectbox("Specify the energy source for the AC unit:", source_options, index=0)
        n_heat = st.number_input("Number of heater equipments: ", min_value=1, value=1)
        p_heat = st.number_input("Heater equipment Wattage (W):", min_value=50, value=ac["1"].iloc[1])
        t_heat = st.slider("Number of hours of heater use per week:", min_value=1, max_value=168, value=0)
        ac_equips = np.append(ac_equips, ["Heater", n_heat, p_heat, t_heat, hac_source])
    
    if "Multi-Split" in type_ac:
        mac_source = st.selectbox("Specify the energy source for the AC unit:", source_options, index=1)
        n_multi = st.number_input("Number of multi-split equipments: ", min_value=1, value=1)
        p_multi = st.number_input("Multi-split equipment Wattage (W):", min_value=50, value=ac["1"].iloc[2])
        t_multi = st.slider("Number of hours of multi-split use per week:", min_value=1, max_value=168, value=4)
        ac_equips = np.append(ac_equips, ["Multi-Split", n_multi, p_multi, t_multi, mac_source])
        
    if "Radiators" in type_ac:
        rac_source = st.selectbox("Specify the energy source for the AC unit:", source_options, index=0)
        n_radi = st.number_input("Number of radiator equipments: ", min_value=1, value=1)
        p_radi = st.number_input("Radiator equipment Wattage (W):", min_value=50, value=ac["1"].iloc[3])
        t_radi = st.slider("Number of hours of radiator use per week:", min_value=1, max_value=168, value=4)
        ac_equips = np.append(ac_equips, ["Radiators", n_radi, p_radi, t_radi, rac_source])
    
    if "Split" in type_ac:
        sac_source = st.selectbox("Specify the energy source for the AC unit:", source_options, index=3)
        n_split = st.number_input("Number of split equipments: ", min_value=1, value=1)
        p_split = st.number_input("Split equipment Wattage (W):", min_value=50, value=ac["1"].iloc[4])
        t_split = st.slider("Number of hours of split equipment use per week:", min_value=1, max_value=168, value=2)
        ac_equips = np.append(ac_equips, ["Split", n_split, p_split, t_split, sac_source])
    
    if "Fan" in type_ac:
        fac_source = st.selectbox("Specify the energy source for the AC unit:", source_options, index=1)
        n_fan = st.number_input("Number of fan equipments: ", min_value=1, value=1)
        p_fan = st.number_input("Fan equipment Wattage (W):", min_value=50, value=ac["1"].iloc[5])
        t_fan = st.slider("Number of hours of fan equipment use per week:", min_value=1, max_value=168, value=6)
        ac_equips = np.append(ac_equips, ["Fan", n_fan, p_fan, t_fan, fac_source])
        st.write("---")


# In[84]:


ac_equips = ac_equips.reshape((int(len(ac_equips)/5), 5))


# In[85]:


equips_total = [tv, lights, laptop, computer, wash, dish, fridge, microwave, oven, cooktop, dhw_t, ac_equips]


# In[86]:


final_arr = np.array([])
for i in equips_total:
    if i.shape[0] >= 1:
        final_arr = np.append(final_arr, i)


# In[87]:


final_df = pd.DataFrame(final_arr.reshape(int(len(final_arr)/5), 5))
#final_df.columns = ["Number of units", "Wattage (W)", "Weekly use (hours)"]


# In[88]:


final_df["Final Energy (Wh)"] = final_df[1].astype(float)*final_df[2].astype(float)*final_df[3].astype(float)


# In[89]:


st.title("Weekly Final Energy (kWh)")
st.metric("", str(round(final_df["Final Energy (Wh)"].sum()/1000)) + " kWh")
st.write("---")


# In[90]:


st.title("Weekly Primary Energy (kWh)")
st.header("Energy conversion")
nat_gas = st.checkbox("Natural Gas plant", value=True)
renew = st.checkbox("Renewables", value=True)
coal = st.checkbox("Coal power plant")
biomass = st.checkbox("Biomass power plant")
st.write("---")


# In[91]:


np.array([])


# In[92]:


nat_gas_primary =np.array(np.array([]))
renew_primary = np.array(np.array([]))
coal_primary = np.array(np.array([]))
biomass_primary = np.array(np.array([]))

percent_gen = np.array(np.array([]))
percent_gen_renew = np.array([])
percent_gen_coal = np.array([])
percent_gen_biomass = np.array([])

efficiency = np.array([])
efficiency_renew = np.array([])
efficiency_coal = np.array([])
efficiency_biomass = np.array([])

if nat_gas:
    st.subheader("Natural Gas Plant")
    percent_gen = np.append(percent_gen,
                            float(st.slider("Natural Gas plant ratio of generation (%)", min_value=0, max_value=100, value=50)))
    efficiency = np.append(efficiency,
                           float(st.slider("Natural Gas plant Efficiency (%)", min_value=0, max_value=100, value=50)))
    nat_gas_primary = np.append(nat_gas_primary, percent_gen*round(final_df["Final Energy (Wh)"].sum()/1000)/efficiency)

if renew:
    st.subheader("Renewables")
    percent_gen_renew = np.append(percent_gen_renew,
                                  float(st.slider("Renewables ratio of generation (%)", min_value=0, max_value=100, value=50)))
    efficiency_renew = np.append(efficiency_renew, 
                                 float(st.slider("Renewables efficiency (%)", min_value=0, max_value=100, value=100)))
    renew_primary = np.append(renew_primary, percent_gen_renew*round(final_df["Final Energy (Wh)"].sum()/1000)/efficiency_renew)
    
if coal:
    st.subheader("Coal power plant")
    percent_gen_coal = np.append(percent_gen_coal, 
                                 float(st.slider("Coal power plant ratio of generation (%)", min_value=0, max_value=100, value=50)))
    efficiency_coal = np.append(efficiency_coal, 
                                float(st.slider("Coal power plant efficiency (%)", min_value=0, max_value=100, value=100)))
    coal_primary = np.append(coal_primary, percent_gen_coal*round(final_df["Final Energy (Wh)"].sum()/1000)/efficiency_coal)

if biomass:
    st.subheader("Biomass power plant")
    percent_gen_biomass = np.append(percent_gen_biomass, 
                                    float(st.slider("Biomass power plant ratio of generation (%)", min_value=0, max_value=100, value=50)))
    efficiency_biomass = np.append(efficiency_biomass, 
                                   float(st.slider("Biomass power plant efficiency (%)", min_value=0, max_value=100, value=100)))
    biomass_primary = np.append(biomass_primary, percent_gen_biomass*round(final_df["Final Energy (Wh)"].sum()/1000)/efficiency_biomass)
    


# In[93]:


arr = np.array(pd.DataFrame((nat_gas_primary, renew_primary, coal_primary, biomass_primary, 
                             efficiency, efficiency_renew, efficiency_coal, efficiency_biomass, 
                             percent_gen, percent_gen_renew, percent_gen_coal, percent_gen_biomass))[0]).reshape(3, 4)


# In[94]:


bar_df = pd.DataFrame(arr).transpose()
bar_df.columns=["Primary Energy (kWh)", "Efficiency", "% generation"]
bar_df.index = ["Natural Gas plant", "Renewables plant", "Coal power plant", "Biomass power plant"]


# In[95]:


bar_df.dropna(inplace=True)


# In[96]:


st.header("Weekly primary total energy (Wh)")


# In[97]:


labels = np.concatenate((final_df[4].unique(), final_df[0], bar_df.dropna().index))


# In[98]:


source_arr = []
target_arr = []
value_arr = []
color_arr = []
for i, m, n in zip(final_df[4], final_df[0], final_df["Final Energy (Wh)"]):
    for j in labels:
        if i == j: #primeiras ligações
            source_arr = np.append(source_arr, list(labels).index(i))
            
            target_arr = np.append(target_arr, list(labels).index(m))
            value_arr = np.append(value_arr, n)
        if m == j:#segundas ligações
            if i == "Electricity":
                for z in bar_df.index:
                    source_arr = np.append(source_arr, list(labels).index(m))
                    target_arr = np.append(target_arr, list(labels).index(z))
                    
                    value_arr = np.append(value_arr, n*bar_df["% generation"][z]/bar_df["Efficiency"][z])
                
            elif i == "Natural Gas":
                    source_arr = np.append(source_arr, list(labels).index(m))
                    target_arr = np.append(target_arr, list(labels).index("Natural Gas plant"))
                    
                    value_arr = np.append(value_arr, n)
                
            
            elif i == "Biomass":
                    source_arr = np.append(source_arr, list(labels).index(m))
                    target_arr = np.append(target_arr, list(labels).index("Biomass power plant"))
                    
                    value_arr = np.append(value_arr, n)
            
            elif i == "Renewables":
                    source_arr = np.append(source_arr, list(labels).index(m))
                    target_arr = np.append(target_arr, list(labels).index("Renewables plant"))
                    
                    value_arr = np.append(value_arr, n)
                                   
            


# In[100]:


source_arr


# In[99]:


import plotly.graph_objects as go

fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = labels,
      customdata = labels,
      hovertemplate='Node %{customdata} has total value %{value}<extra></extra>'
    ),
    link = dict(
      source = source_arr.astype(int), # indices correspond to labels, eg A1, A2, A2, B1, ...
      target = target_arr.astype(int),
      value = value_arr,
      customdata = ["q","r","s","t","u","v"],
      hovertemplate='Link from node %{source.customdata}<br />'+
        'to node%{target.customdata}<br />has value %{value}'+
        '<br />and data %{customdata}<extra></extra>',
  ))])

fig.update_layout(title_text="Energy Sankey Diagram (Wh)", font_size=10)
#fig.show()
st.plotly_chart(fig)


# In[ ]:





# In[ ]:





# In[ ]:




