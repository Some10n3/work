from glapp.PyOGLApp import *
from glapp.LoadMesh import *
from glapp.Light import *

vertex_shader = r'''
#version 330 core
in vec3 position;
in vec3 vertex_color;
in vec3 vertex_normal;
in vec2 vertex_uv;
uniform mat4 projection_mat;
uniform mat4 model_mat;
uniform mat4 view_mat;
out vec3 color;
out vec3 normal;
out vec3 fragpos;
out vec3 view_pos;
out vec2 UV;

void main()
{
    view_pos = vec3(inverse(model_mat) * 
                    vec4(view_mat[3][0], view_mat[3][1], view_mat[3][2], 1));
    gl_Position = projection_mat * inverse(view_mat) * model_mat * vec4(position, 1);
    normal = mat3(transpose(inverse(model_mat))) * vertex_normal;
    fragpos = vec3(model_mat * vec4(position, 1));
    color = vertex_color;
    UV = vertex_uv;
}
'''

fragment_shader = r'''
#version 330 core
in vec3 color;
in vec3 normal;
in vec3 fragpos;
in vec3 view_pos;
out vec4 frag_color;
in vec2 UV;
uniform sampler2D tex;

struct light
{
    vec3 position;
    vec3 color;
};

#define NUM_LIGHTS 3
uniform light light_data[NUM_LIGHTS];

vec4 Create_Light(vec3 light_pos, vec3 light_color, vec3 normal, vec3 fragpos, vec3 view_dir)
{
    // ambient
    float a_strength = 0.3;  // Increased ambient strength
    vec3 ambient = a_strength * light_color;
    
    // diffuse
    vec3 norm = normalize(normal);
    vec3 light_dir = normalize(light_pos - fragpos);
    float diff = max(dot(norm, light_dir), 0);
    vec3 diffuse = diff * light_color;
    
    // specular
    float s_strength = 0.5;
    vec3 reflect_dir = reflect(-light_dir, norm);  // Fixed reflection calculation
    float spec = pow(max(dot(view_dir, reflect_dir), 0), 32);
    vec3 specular = s_strength * spec * light_color;
    
    return vec4(color * (ambient + diffuse + specular), 1);
}

void main()
{
    vec3 view_dir = normalize(view_pos - fragpos);
    frag_color = vec4(0.0);  // Initialize frag_color
    
    for(int i = 0; i < NUM_LIGHTS; i++) {
        frag_color += Create_Light(light_data[i].position, light_data[i].color, normal, fragpos, view_dir);
    }
    
    frag_color = frag_color * texture(tex, UV);
}
'''

class TexturedObjects(PyOGLApp):
    def __init__(self):
        super().__init__(850, 200, 1000, 800)
        self.plane = None
        self.cube = None
        self.granny = None  # New object
        self.light = None
        self.camera = None
        glEnable(GL_CULL_FACE)

    def initialise(self):
        try:
            self.program_id = create_program(vertex_shader, fragment_shader)
            
            # Initialize camera first
            self.camera = Camera(self.program_id, self.screen_width, self.screen_height)
            self.camera.eye = pygame.Vector3(0, 2, 5)  # Position camera to see objects
            self.camera.target = pygame.Vector3(0, 0, 0)
            
            # Create lights
            self.light = Light(self.program_id, pygame.Vector3(0, 3, 2), pygame.Vector3(1, 1, 1), 0)
            
            # Load meshes
            self.plane = LoadMesh("models/plane.obj", "images/window.png", self.program_id,
                                location=pygame.Vector3(0, -1, 0))
            self.cube = LoadMesh("models/cube.obj", "images/crate.png", self.program_id,
                               location=pygame.Vector3(0, 0, 0))
            self.granny = LoadMesh("models/granny.obj", "images/crate.png", self.program_id,  # New object
                               location=pygame.Vector3(1, 0, 0))
            
            # Enable necessary GL features
            glEnable(GL_DEPTH_TEST)
            glEnable(GL_BLEND)
            glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
            
        except Exception as e:
            print(f"Error during initialization: {str(e)}")
            raise

    def display(self):
        glClearColor(0.1, 0.1, 0.1, 1.0)  # Dark gray background
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        glUseProgram(self.program_id)
        
        # Update camera and light
        self.camera.update()
        self.light.update()
        
        # Draw objects
        if self.cube:
            self.cube.draw()
        if self.plane:
            self.plane.draw()
        if self.granny:  # New object
            self.granny.draw()

if __name__ == "__main__":
    TexturedObjects().mainloop()