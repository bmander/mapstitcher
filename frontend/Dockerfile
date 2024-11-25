FROM node:18-alpine

WORKDIR /app

# Create the application directory and set permissions
RUN chown -R node:node /app

# Switch to non-root user
USER node

# Copy package files
COPY --chown=node:node package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY --chown=node:node . .

EXPOSE 3000
CMD ["npm", "start"]
