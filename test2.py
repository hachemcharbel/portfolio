import streamlit as st

# --- Personal Info ---
st.title("Curriculum Vitae - AI & Industry Projects")
st.write("**Name:** YourFirstName YourLastName")
st.write("**LinkedIn:** [linkedin.com/in/yourprofile](https://linkedin.com/in/yourprofile)")

# --- Automotive Projects ---
with st.expander("🚗 Automotive Projects"):
    st.subheader("1. Pilot - Automation of Quality Control of Winding on Hydrogen Tanks")
    st.write("""
    Installed cameras on the carbon fiber winding system for hydrogen tanks to detect visual defects such as overlapping fibers, incorrect fiber angles, and tears.  
    Infrared cameras captured raw data from the heated resin-impregnated fibers. Image processing techniques enabled defect detection.  
    """)
    # Placeholder images
    st.image([
        "https://via.placeholder.com/400x200?text=Hydrogen+Tank+1",
        "https://via.placeholder.com/400x200?text=Hydrogen+Tank+2",
        "https://via.placeholder.com/400x200?text=Hydrogen+Tank+3"
    ])
    st.markdown("[🔗 Project details](https://example.com/hydrogen-tank-project)")

    st.markdown("---")

    st.subheader("2. Pilot - Deployment of HMI to Increase Plants’ Performances")
    st.write("""
    Promoted to IT project manager. Led the deployment of a Human-Machine Interface (HMI) on a production line at Stellantis Sochaux.  
    Responsibilities: technology proposals, system architecture, software modeling, agile development planning and validation.  
    Team: software engineer, PhD student, roboticist, automation engineer.  
    Enhanced project management, leadership, and technical communication skills.  
    """)
    st.markdown("---")

    st.subheader("3. POC - Brick Orientation Adjustment Using Image Processing")
    st.write("""
    Installed a camera to calculate the angle of ceramic bricks and automatically rotate them for correct positioning to avoid damage during assembly.  
    Resulted in a scientific article.  
    """)
    st.image([
        "https://via.placeholder.com/400x200?text=Scientific+Article+1",
        "https://via.placeholder.com/400x200?text=Scientific+Article+2"
    ])
    st.markdown("[🔗 Article IEEE](https://ieeexplore.ieee.org/abstract/document/9803927/)")

    st.markdown("---")

    st.subheader("4. Prototype - Welding Seam Classification Using Data Augmentation")
    st.write("""
    Deployed in 3 Forvia plants across Europe to check weld quality with 5 external defect types.  
    Used data augmentation techniques to compensate for limited data and improve model accuracy.  
    """)
    st.image([
        "https://via.placeholder.com/400x200?text=Welding+Seam+1",
        "https://via.placeholder.com/400x200?text=Welding+Seam+2",
        "https://via.placeholder.com/400x200?text=Welding+Seam+3"
    ])
    st.markdown("[🔗 Article IEEE](https://ieeexplore.ieee.org/abstract/document/9803927/)")

    st.markdown("---")

    st.subheader("5. Pilot - Component Presence Control Using ResNet50 Architecture")
    st.write("""
    Applied component control techniques at Forvia Seating to verify correct component placement, replacement, or absence.  
    Installed late in the production cycle.  
    Presented at a conference in China, awarded best presentation diploma.  
    Resulted in a scientific article.  
    """)
    st.image([
        "https://via.placeholder.com/400x200?text=Component+Control+1",
        "https://via.placeholder.com/400x200?text=Component+Control+2",
        "https://via.placeholder.com/400x200?text=Component+Control+3"
    ])
    st.markdown("[🔗 Article IEEE](https://ieeexplore.ieee.org/abstract/document/9803927/)")

# --- Agriculture Projects ---
with st.expander("🌱 Agriculture Projects"):
    st.write("Please add your agriculture projects here.")

# --- Personal Projects ---
with st.expander("⚙️ Personal Projects"):
    st.write("Please add your personal projects here.")
st.markdown("---")

st.write("**References:**")
st.write("- Reference 1: Name, Position, Email, Phone")
st.write("- Reference 2: Name, Position, Email, Phone")
st.write("- Reference 3: Name, Position, Email, Phone")