// Code generated by Wire protocol buffer compiler, do not edit.
// Source file: business/diary.proto at 37:1
package me.littlekey.duoyu.model.proto;

import com.squareup.wire.FieldEncoding;
import com.squareup.wire.Message;
import com.squareup.wire.ProtoAdapter;
import com.squareup.wire.ProtoReader;
import com.squareup.wire.ProtoWriter;
import com.squareup.wire.WireField;
import com.squareup.wire.internal.Internal;
import java.io.IOException;
import java.lang.Object;
import java.lang.Override;
import java.lang.String;
import java.lang.StringBuilder;
import java.util.List;
import okio.ByteString;

public final class PublishedResponse extends Message<PublishedResponse, PublishedResponse.Builder> {
  public static final ProtoAdapter<PublishedResponse> ADAPTER = new ProtoAdapter_PublishedResponse();

  private static final long serialVersionUID = 0L;

  @WireField(
      tag = 1,
      adapter = "me.littlekey.duoyu.model.proto.Diary#ADAPTER",
      label = WireField.Label.REPEATED
  )
  public final List<Diary> diaries;

  @WireField(
      tag = 2,
      adapter = "me.littlekey.duoyu.model.proto.Cursor#ADAPTER"
  )
  public final Cursor cursor;

  public PublishedResponse(List<Diary> diaries, Cursor cursor) {
    this(diaries, cursor, ByteString.EMPTY);
  }

  public PublishedResponse(List<Diary> diaries, Cursor cursor, ByteString unknownFields) {
    super(ADAPTER, unknownFields);
    this.diaries = Internal.immutableCopyOf("diaries", diaries);
    this.cursor = cursor;
  }

  @Override
  public Builder newBuilder() {
    Builder builder = new Builder();
    builder.diaries = Internal.copyOf("diaries", diaries);
    builder.cursor = cursor;
    builder.addUnknownFields(unknownFields());
    return builder;
  }

  @Override
  public boolean equals(Object other) {
    if (other == this) return true;
    if (!(other instanceof PublishedResponse)) return false;
    PublishedResponse o = (PublishedResponse) other;
    return unknownFields().equals(o.unknownFields())
        && diaries.equals(o.diaries)
        && Internal.equals(cursor, o.cursor);
  }

  @Override
  public int hashCode() {
    int result = super.hashCode;
    if (result == 0) {
      result = unknownFields().hashCode();
      result = result * 37 + diaries.hashCode();
      result = result * 37 + (cursor != null ? cursor.hashCode() : 0);
      super.hashCode = result;
    }
    return result;
  }

  @Override
  public String toString() {
    StringBuilder builder = new StringBuilder();
    if (!diaries.isEmpty()) builder.append(", diaries=").append(diaries);
    if (cursor != null) builder.append(", cursor=").append(cursor);
    return builder.replace(0, 2, "PublishedResponse{").append('}').toString();
  }

  public static final class Builder extends Message.Builder<PublishedResponse, Builder> {
    public List<Diary> diaries;

    public Cursor cursor;

    public Builder() {
      diaries = Internal.newMutableList();
    }

    public Builder diaries(List<Diary> diaries) {
      Internal.checkElementsNotNull(diaries);
      this.diaries = diaries;
      return this;
    }

    public Builder cursor(Cursor cursor) {
      this.cursor = cursor;
      return this;
    }

    @Override
    public PublishedResponse build() {
      return new PublishedResponse(diaries, cursor, super.buildUnknownFields());
    }
  }

  private static final class ProtoAdapter_PublishedResponse extends ProtoAdapter<PublishedResponse> {
    ProtoAdapter_PublishedResponse() {
      super(FieldEncoding.LENGTH_DELIMITED, PublishedResponse.class);
    }

    @Override
    public int encodedSize(PublishedResponse value) {
      return Diary.ADAPTER.asRepeated().encodedSizeWithTag(1, value.diaries)
          + (value.cursor != null ? Cursor.ADAPTER.encodedSizeWithTag(2, value.cursor) : 0)
          + value.unknownFields().size();
    }

    @Override
    public void encode(ProtoWriter writer, PublishedResponse value) throws IOException {
      Diary.ADAPTER.asRepeated().encodeWithTag(writer, 1, value.diaries);
      if (value.cursor != null) Cursor.ADAPTER.encodeWithTag(writer, 2, value.cursor);
      writer.writeBytes(value.unknownFields());
    }

    @Override
    public PublishedResponse decode(ProtoReader reader) throws IOException {
      Builder builder = new Builder();
      long token = reader.beginMessage();
      for (int tag; (tag = reader.nextTag()) != -1;) {
        switch (tag) {
          case 1: builder.diaries.add(Diary.ADAPTER.decode(reader)); break;
          case 2: builder.cursor(Cursor.ADAPTER.decode(reader)); break;
          default: {
            FieldEncoding fieldEncoding = reader.peekFieldEncoding();
            Object value = fieldEncoding.rawProtoAdapter().decode(reader);
            builder.addUnknownField(tag, fieldEncoding, value);
          }
        }
      }
      reader.endMessage(token);
      return builder.build();
    }

    @Override
    public PublishedResponse redact(PublishedResponse value) {
      Builder builder = value.newBuilder();
      Internal.redactElements(builder.diaries, Diary.ADAPTER);
      if (builder.cursor != null) builder.cursor = Cursor.ADAPTER.redact(builder.cursor);
      builder.clearUnknownFields();
      return builder.build();
    }
  }
}
