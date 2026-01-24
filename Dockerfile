FROM alpine:latest
RUN apk add --no-cache clang g++ make postgresql-client git
WORKDIR /app
COPY . .
RUN clang++ baker.cpp -o zenith_baker
CMD ["./zenith_baker"]
